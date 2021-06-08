from ..models import *
from ..data.verse_counts import *

def import_data():
    output = ''

    output += run_job(clear_current_bible_data, 'Clear Bible Data')
    output += run_job(import_all_bible_data, 'Import Bible Data')

    return output

def clear_current_bible_data():
    Testament.objects.all().delete()
    output = sub_job('Deleting Testaments')
    Book.objects.all().delete()
    output += sub_job('Deleting Books')
    Chapter.objects.all().delete()
    output += sub_job('Deleting Chapters')
    Verse.objects.all().delete()
    output += sub_job('Deleting Verses')
    return output

def import_all_bible_data():
    ot = Testament(order=1, name='Old Testament')
    ot.save()
    nt = Testament(order=2, name='New Testament')
    nt.save()
    
    output = ''
    book_num = 0
    testament = ot
    for book_data in passage_data:
        
        if book_data:
            book_name = book_data[0]
            if book_name == 'Matthew':
                testament = nt
            book = Book(name=book_name, testament=testament, order=book_num)
            book.save()
            output += sub_job(f'<b>Book: {book_name}</b>')
            output += sub_job(add_chapters(book_num, book, book_data[2]))
            
        book_num += 1

    return output

def add_chapters(book_num, book, verse_counts):
    output = ''
    chap_index = 1
    while chap_index < len(verse_counts):
        verse_count = verse_counts[chap_index]
        output += f'<b>ch{chap_index}: </b>'
        chapter = Chapter(number=chap_index, book=book)
        chapter.save()
        for verse_num in range(1, verse_count + 1):
            verse_tuple = (book_num, chap_index, verse_num)
            if verse_tuple in omitted_verses:
                output += f'OMITTED '
            else:
                verse = Verse(number=verse_num, chapter=chapter)
                verse.save()
            output += f'v{verse_num}, '
        chap_index += 1
        output += '<br>'
    return output

def run_job(job_func, job_name):
    output = start_job(job_name)
    output += job_func()
    output+= end_job(job_name)
    return output

def start_job(job_name):
    return f'<div class="job-start">Starting: {job_name} </div><br>'

def end_job(job_name):
    return f'<div class="job-end">Completed: {job_name} </div><br>'

def sub_job(name):
    return f'<div class="sub-job">{name}</div><br>'
