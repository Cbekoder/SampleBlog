from django.shortcuts import render
from .models import *
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    content = {
        "maqolalar" : Maqola.objects.all(),
        "yillar" : Maqola.objects.all().values("date").distinct().order_by("date")
    }
    return render(request, 'blog.html', content)

def maqola(request, slug):

    content = {
        "maqola" : Maqola.objects.get(slug = slug)
    }
    return render(request, "maqola.html", content)
