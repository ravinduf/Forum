from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    Author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    Question = models.TextField()
    Votes = models.SmallIntegerField(default = 0)
    added_date = models.DateTimeField()
    
    def __str__(self):
        return self.Question

    def vote(self):
        self.Votes += 1
