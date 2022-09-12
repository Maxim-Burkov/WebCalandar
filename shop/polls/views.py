from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from .models import SimpleUser

def check_user(request):
    user = User.objects.filter(id=1)
    return render(request, 'polls/post_list.html', {'users': user})

def redirected(request):
    user = SimpleUser.objects.all()
    return render(request, 'polls/redirected.html', {'users': user})

def registration(request):
    return render(request, 'polls/registration.html', {})

def create(request):
    if request.method == "POST":
        simple_user = SimpleUser()
        simple_user.first_name = request.POST.get("first_name")
        simple_user.last_name = request.POST.get("last_name")
        simple_user.email = request.POST.get("email")
        simple_user.password = request.POST.get("password")
        simple_user.save()
    return HttpResponseRedirect("/burkoff/redirected")


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")