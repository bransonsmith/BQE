from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
from .data import concordance

app_name = 'glossary'

def index(request):
    output = ''
    output = '<style>body: { width: 100%; height: fit_content; display: flex; flex-direction: column;} .out { box-shadow: 2px 2px 7px #565658; width: 700px; max-width: calc(100% - 40px); padding: 20px; margin: 50px auto 0px; min-height: 100px; background-color: #fafafb; } .title { font-size: 20px; width: fit-content; margin: auto auto 15px auto; } .content { font-size: 14px; } .job-start { font-size: 14px; font-weight: bold; background-color: #defcfc; } .job-end { font-size: 14px; font-weight: bold; background-color: #daf8f8; margin-bottom: 40px; } .sub-job { padding-left: 20px; }</style>'
    output += '<div class="out">'
    output += '<div class="title">{app_name} data</div>'
    output += '<div class="content">'
    output += f'To seed the {app_name} data 1) navigate to <a href="./delete_{app_name}">/{app_name}/delete_{app_name}</a> 2) navigate to <a href="./seed_{app_name}">/{app_name}/seed_{app_name}</a>'
    output += "</div></div>"
    return HttpResponse(output)

def delete_glossary(request):
    print('Deleting Words')
    Word.objects.all().delete()
    print('Deleted Words')

    return HttpResponse(f'Deleted all {app_name} data.<br>Go to <a href="./seed_{app_name}">{app_name}/seed_{app_name}</a> to seed the {app_name} data (this may take a few minutes).')

def seed_glossary(request):
    desired_number_of_words = len(concordance.words)
    num_words_to_add_in_each_call = 1000
    word_count = len(list(Word.objects.all()))

    print(f'Importing {app_name} - Word count before: {word_count}')
    print(f'Importing {num_words_to_add_in_each_call} more words.')

    words_imported_this_call = 0
    while words_imported_this_call < num_words_to_add_in_each_call and (words_imported_this_call + word_count) < desired_number_of_words:
        next_word_data = concordance.words[words_imported_this_call + word_count]
        new_word = Word(name=next_word_data["name"])
        new_word.save()
        for entry_data in next_word_data["entrys"]:
            new_entry = Entry(word=new_word, book=entry_data["book"], chapter=entry_data["chapter"], verse=entry_data["verse"])
            new_entry.save()
        words_imported_this_call += 1
    
    print(f'Added {words_imported_this_call} words. Last word = {next_word_data["name"]}')

    if (words_imported_this_call + word_count) < desired_number_of_words:
        return redirect(f'./seed_glossary')

    print(f'Seeded {app_name}')
    return (HttpResponse(f'Done seeding {app_name} data'))
