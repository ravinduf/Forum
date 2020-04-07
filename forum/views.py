from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
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
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.addTime()
            answer.save()
            return HttpResponseRedirect("")
        else:
            return HttpResponse('hello world')
    return render(request, 'forum/question_page.html',{ 'question': question , 'form': form} )

def addVote(request,pk):
    question = get_object_or_404 (Question, pk=pk)
    question.votes += 1
    question.save()
    return redirect('question_details', pk = question.pk) #you have to give the urlpattern name instead of view function and 
                                                        #always remember to give simillar names for them

def subVote(request,pk):
    question = get_object_or_404 (Question, pk=pk)
    question.votes -= 1
    question.save()
    return redirect('question_details', pk = question.pk)