from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.
class Word(models.Model):
    name = models.CharField(max_length=77)

class Entry(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    book = models.CharField(max_length=77)
    chapter = models.IntegerField(default=0)
    verse = models.IntegerField(default=0)