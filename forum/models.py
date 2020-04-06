from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete = models.CASCADE)
    question = models.TextField()
    votes = models.SmallIntegerField(default = 0)
    added_date = models.DateTimeField()
    
    def __str__(self):
        return self.question

    def vote(self):
        self.Votes += 1

class answer(models.Model):
    question = models.ForeignKey('forum.Question' ,on_delete = models.CASCADE, related_name = 'answer')
    author = models.CharField(max_length=50)
    answer = models.TextField()
    votes = models.SmallIntegerField(default = 0)
    added_date = models.DateTimeField()

    def __str__(self):
        return self.answer
    
    def vote(self):
        self.Votes += 1