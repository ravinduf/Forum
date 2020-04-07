from django import forms
from django.forms import ModelForm

from .models import *

class answerForm(forms.ModelForm):

    class Meta:
        model = answer
        fields = ('answer',)