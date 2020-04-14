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
    v = Votes.objects.filter(voter = request.user.username, question = question)
    if v.count() == 0:
        v = Votes.objects.create(question = question, voter = request.user.username)
        v.status = True
        v.save()
        question.votes_count += 1
        question.save()
        return redirect('question_details', pk = question.pk) #you have to give the urlpattern name instead of view function and 
                                                                #always remember to give simillar names for them

    elif v.count() == 1:
        v = Votes.objects.get(voter = request.user.username, question = question)
        status = v.status
        if status == False:
            v.status = None
            question.votes_count += 1
            
        elif status == None:
            v.status = True
            question.votes_count += 1

        
        v.save()
        question.save()
        return redirect('question_details', pk = question.pk)
    
    else:
        return redirect('question_details', pk = question.pk)
    
        
     
def subVote(request,pk):
    question = get_object_or_404 (Question, pk=pk)
    v = Votes.objects.filter(voter = request.user.username, question = question)
    if v.count() == 0:
        v = Votes.objects.create(question = question, voter = request.user.username)
        v.status = False
        v.save()
        question.votes_count -= 1
        question.save()
        return redirect('question_details', pk = question.pk)
    
    elif v.count() == 1:
        v = Votes.objects.get(voter = request.user.username, question = question)
        status = v.status
        if status == True:
            v.status = None
            question.votes_count -= 1
        elif status == None:
            v.status = False
            question.votes_count -= 1
        v.save()
        question.save()
        return redirect('question_details', pk = question.pk)
    
    
    return redirect('question_details', pk = question.pk)

def addQuestion(request):
    if request.method == 'POST':
        form = questionForm(request.POST)
        if form.is_valid():
            question = form.save(commit = False)
            question.author = request.user
            question.addTime()
            question.save()
            return redirect('/')
    
    else:
        form = questionForm()
        return render(request, 'forum/add_question.html',{'form' : form})