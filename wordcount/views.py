from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    word = 'hello this is joshua and he is a ugandan'
    counter = 0
    for i in word.split():
        counter+=1
    return HttpResponse (counter)

def index(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist)})

def about(request):
    return render(request, 'about.html')