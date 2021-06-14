from django.shortcuts import redirect
from django.http import HttpResponse
from .services.import_bible_data import import_data
from .models import *
from .data.verse_counts import *
import os

def production_check():
    try:
        if os.environ['NOT_PRODUCTION'] != 'True':
            raise Exception()
    except:
        raise Exception('You can\'t do that here. The environment variable: NOT_PRODUCTION must have a value of \'True\' for data scripts to be run.')

def delete_bible_data(request):
    production_check()
    num = 100
    if len(Chapter.objects.all()) > num:
        Chapter.objects.filter(id__in=list(Chapter.objects.values_list('pk', flat=True)[:num])).delete()
    else:
        Chapter.objects.all().delete()
    
    if len(Chapter.objects.all()) > 0:
        return redirect('delete_bible_data')
    return redirect('delete_testaments')

def delete_testaments(request):
    production_check()
    Testament.objects.all().delete()
    return HttpResponse('Deleted all Bible Data.')

def seed_bible_data(request):
    production_check()
    ot = Testament(order=1, name='Old Testament')
    ot.save()
    nt = Testament(order=2, name='New Testament')
    nt.save()

    return redirect('seed_books')

def seed_books(request):
    production_check()
    num_uploaded = 0
    num_books = len(list(Book.objects.all()))
    book_num = num_books
    for book_data in passage_data[num_books:]:
        testament = None
        if book_num <= 49:
            testament = Testament.objects.all().filter(name="Old Testament").first()
        else:
            testament = Testament.objects.all().filter(name="New Testament").first()

        if book_data:
            book_name = book_data[0]
            book = Book(name=book_name, testament=testament, order=book_num)
            try:
                book.save()
                add_chapters(book_num, book, book_data[2])
            except:
                pass
        
        num_uploaded += 1
        book_num += 1
        if num_uploaded > 10:
            return redirect('seed_books')

    return HttpResponse('Done Seeding Bible Data.')

def add_chapters(book_num, book, verse_counts):
    output = ''
    chap_index = 1
    while chap_index < len(verse_counts):
        verse_count = verse_counts[chap_index]
        chapter = Chapter(number=chap_index, book=book)
        chapter.save()
        for verse_num in range(1, verse_count + 1):
            verse_tuple = (book_num, chap_index, verse_num)
            if verse_tuple not in omitted_verses:
                verse = Verse(number=verse_num, chapter=chapter)
                verse.save()
        chap_index += 1
    return output


