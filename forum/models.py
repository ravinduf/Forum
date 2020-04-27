from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete = models.CASCADE)
    title = models.CharField(max_length=200,blank = True, null = True)
    question = models.TextField()
    votes_count = models.SmallIntegerField(default = 0)
    added_date = models.DateTimeField()
    
    def __str__(self):
        return self.title

    def vote(self):
        self.Votes += 1

    def addTime(self):
        self.added_date = timezone.now()

class answer(models.Model):
    question = models.ForeignKey('forum.Question' ,on_delete = models.PROTECT, related_name = 'answer')
    author = models.CharField(max_length = 50)
    answer = models.TextField()
    votes_count = models.SmallIntegerField(default = 0)
    added_date = models.DateTimeField()

    def __str__(self):
        return str(self.answer)
    
    def vote(self):
        self.Votes += 1

    def addTime(self):
        self.added_date = timezone.now()

class Votes(models.Model):
    question = models.ForeignKey('forum.Question' ,on_delete = models.PROTECT, related_name = 'votes')
    voter = models.CharField(max_length = 50)
    status = models.BooleanField(null = True, blank = True) #true for upvote and false for downvote and none for not voted

    def __str__(self):
        return self.voter

class answerVotes(models.Model):
    answer = models.ForeignKey('forum.answer', on_delete = models.PROTECT, related_name = 'votes_answer')
    question = models.ForeignKey('forum.Question', on_delete = models.PROTECT, related_name = 'votes_answer_question')
    voter = models.CharField(max_length = 50)
    status = models.BooleanField(null = True, blank = True)

    def __str__(self):
        return self.voter
