from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    questions = Question.objects.order_by('added_date').reverse()

    return render(request, 'forum/home_page.html',{'questions' : questions })
