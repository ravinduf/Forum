from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(answer)
admin.site.register(Votes)
admin.site.register(answerVotes)