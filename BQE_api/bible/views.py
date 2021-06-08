from django.shortcuts import render
from django.http import HttpResponse
from .services.import_bible_data import import_data

def index(request):
    output = '<style>body: { width: 100%; height: fit_content; display: flex; flex-direction: column;} .out { box-shadow: 2px 2px 7px #565658; width: 700px; max-width: calc(100% - 40px); padding: 20px; margin: 50px auto 0px; min-height: 100px; background-color: #fafafb; } .title { font-size: 20px; width: fit-content; margin: auto auto 15px auto; } .content { font-size: 14px; } .job-start { font-size: 14px; font-weight: bold; background-color: #defcfc; } .job-end { font-size: 14px; font-weight: bold; background-color: #daf8f8; margin-bottom: 40px; } .sub-job { padding-left: 20px; }</style>'
    output += '<div class="out">'
    output += '<div class="title">Bible Data Import View</div>'
    output += '<div class="content">'
    output += import_data()
    output += "</div></div>"
    return HttpResponse(output)
