from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome dear!")

def test(request):
    with open('todo_app/front/list.html', 'r') as html_file:
        html_content = html_file.read()
    
    return HttpResponse(html_content, content_type='text/html')