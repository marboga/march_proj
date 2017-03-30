from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Location, Activity, Lockbox

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreatorForm

# Create your views here.
def index(request):

    context = {
        'locations': Location.objects.all(),
        'activities': Activity.objects.all(),
        'boxes': Lockbox.objects.all(),
        'form': UserCreatorForm(),
        'users': User.objects.all(),
    }

    for location in context['locations']:
        print "locations ---", location.spoken_languages
    #
    # for key, val in context.items():
    #     print key
    #     print val
    #     for obj in val:
    #         print obj.id

    return render(request, 'theme_app/index.html', context)

def process(request):
    print "in process", request.POST
    print "views", request.POST['name']

    #(True, obj)
    #(False, error_list)
    valid, response = Location.objects.validate_location(request.POST)
    if valid is True:
        request.session.name = response.name
        print "location created===>", response.id
    else:
        for error in response:
            print error
            messages.error(request, error)
    #call a function in Models
    # my_variable = 2
    # what_comes_back = invocation()
    # print type(what_comes_back)
    # print my_variable
    return redirect('theme_app:index')

def create_activity(request):
    if request.method == 'POST':
        #do our logic
        print request.POST, "<<<<<<---- request.POST"
        valid, response = Activity.objects.validate_activity(request.POST)

        if valid:
            print "woop made it, ", response
            return redirect('theme_app:index')
        else:
            for error in response:
                messages.error(request, error)

    return redirect('theme_app:index')

def lockbox(request):
    if request.method == 'POST':
        print request.POST

        valid, response = Lockbox.objects.validate_lockbox(request.POST)
        if valid:
            pass
        else:
            for error in response:
                messages.error(request, error)


    return redirect('theme_app:index')

def show(request, id):
    print "in show method, id=", id
    context = {
        'location': Location.objects.filter(id=id)
    }
    return render(request, 'theme_app/show.html', context)

def create_user(request):
    form = UserCreationForm(request.POST)
    print form
    print form.is_valid()
    if form.is_valid():
        user = form.cleaned_data.save()
        # user.save()
        print user.username, "<<- username"

    return redirect('theme_app:index')
