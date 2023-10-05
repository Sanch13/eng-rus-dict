from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .models import EngRusWord
from .forms import AddWord


def home(request):
    tittle = "My dictionary"
    context = {
        "title": tittle
    }
    return render(request=request,
                  template_name="dictionary/home.html",
                  context=context)


def words_list(request):
    words = EngRusWord.objects.all()
    context = {
        "words": words
    }
    return render(request=request,
                  template_name="dictionary/words_list.html",
                  context=context)


class AddWordView(View):
    def get(self, request):
        form = AddWord()
        context = {
            "form": form
        }
        return render(request=request,
                      template_name="dictionary/add_word.html",
                      context=context)

    def post(self, request):
        form = AddWord(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dictionary:home'))
        else:
            print(form.errors)
