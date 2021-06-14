from django.shortcuts import redirect
from django.http import HttpResponse
from .services.import_bible_data import import_data
from .models import *
from .data.verse_counts import *

def index(request):
    output = '<style>body: { width: 100%; height: fit_content; display: flex; flex-direction: column;} .out { box-shadow: 2px 2px 7px #565658; width: 700px; max-width: calc(100% - 40px); padding: 20px; margin: 50px auto 0px; min-height: 100px; background-color: #fafafb; } .title { font-size: 20px; width: fit-content; margin: auto auto 15px auto; } .content { font-size: 14px; } .job-start { font-size: 14px; font-weight: bold; background-color: #defcfc; } .job-end { font-size: 14px; font-weight: bold; background-color: #daf8f8; margin-bottom: 40px; } .sub-job { padding-left: 20px; }</style>'
    output += '<div class="out">'
    output += '<div class="title">Bible Data Import View</div>'
    output += '<div class="content">'
    output += import_data()
    output += "</div></div>"
    return HttpResponse(output)

def delete_chapters(request):
    num = 100
    if len(Chapter.objects.all()) > num:
        Chapter.objects.filter(id__in=list(Chapter.objects.values_list('pk', flat=True)[:num])).delete()
    else:
        Chapter.objects.all().delete()
    
    if len(Chapter.objects.all()) > 0:
        return redirect('delete_chapters')
    return redirect('delete_bible_data')

def delete_bible_data(request):
    Testament.objects.all().delete()
    return HttpResponse('Deleted all Testaments.')

def seed_bible_data(request):
    ot = Testament(order=1, name='Old Testament')
    ot.save()
    nt = Testament(order=2, name='New Testament')
    nt.save()

    return redirect('seed_books')

def seed_books(request):
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

    return HttpResponse('Seeded all Books.')

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


