from django.db import models

class Testament(models.Model):
    name = models.CharField(max_length=77, unique=True)
    order = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=77, unique=True)
    order = models.IntegerField(default=0)
    testament = models.ForeignKey(Testament, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Chapter(models.Model):
    number = models.IntegerField(default=0)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.book.name} {self.number}'

class Verse(models.Model):
    number = models.IntegerField(default=0)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.chapter.book.name} {self.chapter.number}: {self.number}'
