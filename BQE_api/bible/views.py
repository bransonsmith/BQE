from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
from .data.verse_counts import *

app_name = 'bible';

def index(request):
    output = ''
    output = '<style>body: { width: 100%; height: fit_content; display: flex; flex-direction: column;} .out { box-shadow: 2px 2px 7px #565658; width: 700px; max-width: calc(100% - 40px); padding: 20px; margin: 50px auto 0px; min-height: 100px; background-color: #fafafb; } .title { font-size: 20px; width: fit-content; margin: auto auto 15px auto; } .content { font-size: 14px; } .job-start { font-size: 14px; font-weight: bold; background-color: #defcfc; } .job-end { font-size: 14px; font-weight: bold; background-color: #daf8f8; margin-bottom: 40px; } .sub-job { padding-left: 20px; }</style>'
    output += '<div class="out">'
    output += f'<div class="title">{app_name} data</div>'
    output += '<div class="content">'
    output += f'To seed the {app_name} data 1) navigate to <a href="./delete_bible">/{app_name}/delete_bible</a> 2) navigate to <a href="./seed_bible">/{app_name}/seed_bible</a>'
    output += "</div></div>"
    return HttpResponse(output)

def delete_bible(request):
    num_chapters_to_delete_in_each_run = 100
    number_of_chapters_at_start = len(Chapter.objects.all())
    print(f'Deleting {max(num_chapters_to_delete_in_each_run, number_of_chapters_at_start)} chapters.')
    
    if  number_of_chapters_at_start> num_chapters_to_delete_in_each_run:
        Chapter.objects.filter(id__in=list(Chapter.objects.values_list('pk', flat=True)[:num_chapters_to_delete_in_each_run])).delete()
    else:
        Chapter.objects.all().delete()
    
    if len(Chapter.objects.all()) > 0:
        return redirect('delete_bible')
    
    Testament.objects.all().delete()
    return HttpResponse(f'Deleted all {app_name} data.<br>Go to <a href="./seed_bible">{app_name}/seed_bible</a> to seed the {app_name} data (this may take a few minutes).')

def seed_bible(request):
    ot = Testament(order=1, name='Old Testament')
    ot.save()
    nt = Testament(order=2, name='New Testament')
    nt.save()

    print('Added Testaments.')
    return redirect('seed_books')

def seed_books(request):
    desired_number_of_books = len(passage_data)
    num_books_to_add_in_each_call = 6
    book_count = len(list(Book.objects.all()))

    print(f'Importing {app_name} - Book count before: {book_count}')
    print(f'Importing {num_books_to_add_in_each_call} more books.')

    num_books_added_this_call = 0
    while num_books_added_this_call < num_books_to_add_in_each_call and (num_books_added_this_call + book_count) < desired_number_of_books:
        current_book_index = book_count + num_books_added_this_call
        next_book_data = passage_data[current_book_index]
        testament_name = "Old Testament" if current_book_index < 49 else "New Testament"
        testament = Testament.objects.all().filter(name=testament_name).first()
        book_number = current_book_index + 1
        new_book = Book(testament=testament, name=next_book_data[0], order=book_number)
        new_book.save()
        add_chapters(book_number, new_book, next_book_data[2])
        num_books_added_this_call += 1

    print(f'Added {num_books_added_this_call} books. Last book = {next_book_data[0]}')
    if book_number < desired_number_of_books:
        return redirect('seed_books')

    print(f'Seeded {app_name}')
    return HttpResponse(f'Done seeding {app_name} data.')

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


