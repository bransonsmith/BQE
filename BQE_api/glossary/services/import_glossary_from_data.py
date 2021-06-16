from .concord import words
from ..models import *


def try_this():
    for word in words:
        name = word['name']
        print(name)

def clear_words_from_db():
    Word().objects.all().delete()
    print('DELETING WORDS...')
    Entry().objects.all().delete()
    print('DELETING ENTRIES...')

def import_concord_words():
    for word_data in words:
        word = word_data['name']
        content = Word(name=word)
        content.save()
        print(word)
        print(content)
        entrys = word_data['entrys']
        for entry_data in entrys:
            book = entry_data['book']
            chapter = entry_data['chapter']
            verse = entry_data['verse']
            print(book,chapter,verse)
            entry= Entry(word = content,book=book,chapter=chapter,verse=verse)
            entry.save()
