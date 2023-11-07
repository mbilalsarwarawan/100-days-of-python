from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse("""<h1>Hello my first django app</h1>""")

def success_page(request):
    return render(request,"pages/success-story.html")