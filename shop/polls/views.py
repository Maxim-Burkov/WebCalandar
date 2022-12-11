from django.shortcuts import render
from django.contrib.auth.models import User, Group

from django.utils import timezone


from django.http import HttpResponse, HttpResponseRedirect
from .models import Person, Event

def standart_profile(request, id):
    return render(request, 'polls/standart_profile.html')

def index(request):
    if request.user == 'AnonymousUser':
        return HttpResponse('Анонимус юзер')
    external_id = request.user.id
    event_exist = Event.objects.filter(external_id=external_id)
    return render(request, 'polls/burkoff_shop.html', {'events': event_exist})

def regging(request):
    return render(request, 'polls/regging.html')

def create(request):
    group = Group.objects.get(name='none_prime_users')
    if request.method == "POST":
        nickname = request.POST.get("nickname")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        is_staff = False

        user = User.objects.create_user(username=nickname,
                                        email=email,
                                        password=password,
                                        first_name=first_name,
                                        last_name=last_name,
                                        is_staff=is_staff)

        user.groups.add(group)
        return render(request, 'polls/regging_done.html', {'nickname': nickname})
    else:
        return HttpResponse('Error in registration. Just watch your username or check code')


def create_event(request):
    return render(request, 'polls/create_event.html')

def check_event(request):
    if request.method == "POST":
        event = Event()
        event.external_id = request.user.id
        event.name = request.POST.get("name")
        event.text = request.POST.get("text")
        event.date = request.POST.get("date")

        event.save()
        return HttpResponseRedirect('/burkoff')
    else:
        return HttpResponse('Error in adding event')

def redacting(request, id):
    external_id = request.user.id
    event_id = id
    event_exist = Event.objects.filter(external_id=external_id, id=event_id)
    return render(request, 'polls/redacting.html', {'events': event_exist})

def delete_event(request, id):
    external_id = request.user.id
    event_id = id

    event = Event.objects.filter(external_id=external_id, id=event_id)
    event.delete()
    return HttpResponseRedirect('/burkoff')

def redacting_event(request, id):
    if request.method == 'POST':
        event = Event()
        external_id = request.user.id
        event_id = id
        event.name = request.POST.get("name")
        event.text = request.POST.get("text")
        event.date = request.POST.get("date")

        event_red = Event.objects.filter(external_id=external_id, id=event_id).update(name=event.name,
                                                                                      text=event.text,
                                                                                      )
        return HttpResponseRedirect("/burkoff")


def check_redactor(request, id):
    pass


def email_message(request, email=None):
    pass