from django.shortcuts import render
from django.http import HttpResponseRedirect
from markdown2 import Markdown
from django import forms
from django.urls import reverse
import random


from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label='Title')
    content = forms.CharField(label='Content', widget=forms.Textarea)

titles = util.list_entries()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    page = util.get_entry(title)
    markdowner = Markdown()
    converted = markdowner.convert(page)
    if (page == None):
        return 'Error 404 not found'
    return render(request, 'encyclopedia/title.html', {
        'title': title,
        'page': converted
    })

def search(request):
    query = request.POST['query']
    query = query.capitalize()
    entries = util.list_entries()
    results = []
    for i in entries:
        if query in i:
            results.append(i)
    return render(request, "encyclopedia/results.html", {
        'results': results
        })

def newPage(request):
    if request.method == 'POST':
        page = NewPageForm(request.POST)
        if page.is_valid():
            title = page.cleaned_data['title'].capitalize()
            content = page.cleaned_data['content']
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'encyclopedia/newpage.html', {
                'form': page
            })

    return render(request, "encyclopedia/newpage.html", {
        'form': NewPageForm()
    })

def randomPage(request):
    randomPage = random.choice(titles)
    page = util.get_entry(randomPage)
    markdowner = Markdown()
    converted = markdowner.convert(page)
    return render(request, 'encyclopedia/title.html', {
        'title': randomPage,
        'page': converted
    })