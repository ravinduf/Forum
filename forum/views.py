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
    v = Votes.objects.filter(voter = request.user.username, question = question)
    status = None
    if v.count() == 0:
        status = None
    elif v.count() == 1:
        v = Votes.objects.get(voter = request.user.username, question = question)
        if v.status == True:
            status = True
        elif v.status == False:
            status = False
        else:
            status == None    


    av = answerVotes.objects.filter(voter = request.user.username, question = question)
    answerDict = {}
    if av.count() >= 1:
        for i in av:
            answerDict[str(i.answer.answer)] = i.status
    
    

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
    return render(request, 'forum/question_page.html',{ 'question': question , 'form': form, 'status': status, 'answerDict': answerDict} )

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
    
    else:
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

def questionDelete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return redirect('/')

def answerDelete(request, pk):
    ans = get_object_or_404(answer, pk=pk )
    question = ans.question
    ans.delete()
    return redirect('question_details', pk = question.pk )


def addAnswerVote(request, pk):
    ans = get_object_or_404 (answer, pk=pk)
    question = ans.question
    v = answerVotes.objects.filter(voter = request.user.username, answer = ans, question = question)
    if v.count() == 0:
        v = answerVotes.objects.create(answer = ans, question = question, voter = request.user.username)
        v.status = True
        v.save()
        ans.votes_count += 1
        ans.save()
        return redirect('question_details', pk = question.pk) #you have to give the urlpattern name instead of view function and 
                                                                #always remember to give simillar names for them

    elif v.count() == 1:
        v = answerVotes.objects.get(voter = request.user.username, question = question, answer = ans)
        status = v.status
        if status == False:
            v.status = None
            ans.votes_count += 1
            
        elif status == None:
            v.status = True
            ans.votes_count += 1
        
        
        v.save()
        ans.save()
        return redirect('question_details', pk = question.pk)
    
    

def subAnswerVote(request, pk):
    ans = get_object_or_404 (answer, pk=pk)
    question = ans.question
    v = answerVotes.objects.filter(voter = request.user.username, question = question, answer = ans)
    if v.count() == 0:
        v = answerVotes.objects.create(question = question, answer = ans, voter = request.user.username)
        v.status = False
        v.save()
        ans.votes_count -= 1
        ans.save()
        return redirect('question_details', pk = question.pk)
    
    elif v.count() == 1:
        v = answerVotes.objects.get(voter = request.user.username, answer = ans)
        status = v.status
        if status == True:
            v.status = None
            ans.votes_count -= 1
        elif status == None:
            v.status = False
            ans.votes_count -= 1

        v.save()
        ans.save()
        return redirect('question_details', pk = question.pk)
    
    else:
        return redirect('question_details', pk = question.pk)

def editQuestion(request, pk):
    question = get_object_or_404(Question, pk = pk)
    if request.method == "POST":
        form = questionForm(request.POST, instance = question)
        if form.is_valid():
            form.save()
            return redirect('question_details', pk = question.pk)

    else:
        form = questionForm(instance = question)
    return render(request, 'forum/editQuestion.html', {'form': form})