from django import forms
from .models import EngRusWord


class AddWord(forms.ModelForm):

    class Meta:
        model = EngRusWord
        fields = ("eng", "rus", "description")
