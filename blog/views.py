from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'John Doe',
        'title': 'Post 1',
        'content': 'First contents',
        'date_published': 'August 21, 2018'
    },
    {
        'author': 'John Doe',
        'title': 'Post 1',
        'content': 'First contents',
        'date_published': 'August 21, 2018'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
