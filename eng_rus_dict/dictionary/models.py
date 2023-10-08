from django.db import models


class EngRusWord(models.Model):
    eng = models.CharField(max_length=1000)
    rus = models.CharField(max_length=1000)
    description = models.TextField(blank=True)

