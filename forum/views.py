from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from .forms import *
# Create your views here.
def index(request):
    questions = Question.objects.order_by('added_date').reverse()
    
    return render(request, 'forum/home_page.html',{'questions' : questions })

def question_info(request, pk):
    question = get_object_or_404(Question, pk=pk)
    form = answerForm()

    if request.method == 'POST':
        form = answerForm(request.POST)
        if form.is_valid():
            form.save()
            answer = answer.objects.all().last()
            answer.addTime()
            return redirect('/')
    return render(request, 'forum/question_page.html',{ 'question': question , 'form': form} )
