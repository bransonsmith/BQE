from django.db import models

class Word(models.Model):
    name = models.CharField(max_length=77)
    def __str__(self):
        return self.name
        
class Entry(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    book = models.CharField(max_length=77)
    chapter = models.IntegerField(default=0)
    verse = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.word} {self.book} {self.chapter}: {self.verse}'

class Answer:
    def __init__(self, word: str, book: str, chapter: int, verse: int):
        self.word = word
        self.book = book
        self.chapter = chapter
        self.verse = verse

    def __str__(self):
        return f'{self.word} is in {self.book} {self.chapter}:{self.verse}'
