from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.db.models.functions import Length
import os
from .models import Profile, Experience
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    return render(request, 'login.html')


def error404(request):
    pass


@login_required
def home(request):
    if request.method == 'GET':
        if request.user and not request.user.is_anonymous:
            logged_in = True
        else:
            logged_in = False
        if logged_in:
            user = User.objects.filter(username=request.user.username).first()
            experiences = Experience.objects.all()
            context = {
                'experiences': experiences,
                'user': user,
                'logged_in': logged_in
            }
            return render(request, 'home.html', context)
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        if request.user and not request.user.is_anonymous:
            logged_in = True
        else:
            logged_in = False
        if logged_in:
            user = User.objects.filter(username=request.user.username).first()
            experiences = Experience.objects.all()
            context = {
                'experiences': experiences,
                'user': user,
                'logged_in': logged_in
            }
            return render(request, 'home.html', context)
        else:
            return HttpResponseRedirect(reverse('login'))



