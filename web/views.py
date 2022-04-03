from web.models import Subject
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    context['subjects'] = Subject.objects.all()
    return render(request, "index.html", context)

def detail(request, id):
    context = {}
    subjects = Subject.objects.filter(id=id)
    for subject in subjects:
        context['subject'] = subject
    return render(request, "detail.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


