from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    fruits = [
        {"fruit": "apple", "color": "red"},
        {"fruit": "banana", "color": "yellow"},
        {"fruit": "grape", "color": "purple"},
        {"fruit": "orange", "color": "orange"},
        {"fruit": "watermelon", "color": "green"}
    ]
    return render(request, "pages/success-story.html",context={'fruits' : fruits})


def main(request):
    return HttpResponse("""<h1>Hello my first django app</h1>""")

def success_page(request):
    return render(request,"pages/success-story.html")