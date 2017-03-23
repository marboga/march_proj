from django.shortcuts import render, redirect
from .models import Language
from ..theme_app.models import Location

# Create your views here.
def index(request):
    context = {
        "languages": Language.objects.all(),
        "locations": Location.objects.all(),
    }
    return render(request, 'languages/index.html', context)

def process(request):
    print "here in languages_app:process"
    if request.method == 'POST':
        print request.POST
        response = Language.objects.add_location_to_language(request.POST)
        print response.name, response.locations_spoken.all()
    return redirect('languages_app:index')

def new(request):
    print "here in languages_app:new"
    if request.method == 'POST':
        print request.POST
        res = Language.objects.create_lang(request.POST)
        print "response back to views ==", res

    return redirect('languages_app:index')
