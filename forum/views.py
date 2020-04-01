from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def index(request):
    questions = Question.objects.order_by('added_date').reverse()
    
    return render(request, 'forum/home_page.html',{'questions' : questions })

def question_info(request, pk):
    question = get_object_or_404(Question, pk=pk)

    return render(request, 'forum/question_page.html',{ 'question': question })
