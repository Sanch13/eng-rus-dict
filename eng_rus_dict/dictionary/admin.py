from django.contrib import admin

from .models import EngRusWord


@admin.register(EngRusWord)
class MyEngRusWords(admin.ModelAdmin):
    list_display = ["rus", "eng", "description"]
