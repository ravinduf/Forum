from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Voter(models.Model):
    name = models.CharField(max_length = 50)
    vote_status = models.BooleanField() #True for upcote and False for downvote 
    def __str__(self):
        return self.name
        

class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete = models.CASCADE)
    question = models.TextField()
    votes = models.SmallIntegerField(default = 0)
    added_date = models.DateTimeField()
    voters = models.ManyToManyField(Voter,blank = True)
    
    
    def __str__(self):
        return self.question

    def vote(self):
        self.Votes += 1

    def addTime(self):
        self.added_date = timezone.now()

class answer(models.Model):
    question = models.ForeignKey('forum.Question' ,on_delete = models.CASCADE, related_name = 'answer')
    author = models.CharField(max_length = 50)
    answer = models.TextField()
    votes = models.SmallIntegerField(default = 0)
    added_date = models.DateTimeField()

    def __str__(self):
        return self.answer
    
    def vote(self):
        self.Votes += 1

    def addTime(self):
        self.added_date = timezone.now()

