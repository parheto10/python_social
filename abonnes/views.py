# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string, get_template
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
#from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required,user_passes_test

from .models import Profile, Langage
from .forms import ProfileForm, UserUpdate, EditProfileForm, UserRegistration, LoginForm


def home(request):
    context = {}
    return render(request, 'home.html', context)

@login_required
def dashboard(request):
    return render(request, "abonnes/dashboard.html")

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Bienvenus Sur Codons en Python fr')
                    return redirect('params:home')
                else:
                    #return HttpResponse('Compte Désactiver')
                    messages.error(request, 'Compte Désactiver')
                    return redirect('params:login')
            else:
                messages.error(request, 'Paramètres de Conexion Invalide, Merci de Réessayer SVP !!!')
                return redirect('params:login')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'abonnes/login.html', context)


def add_profile(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)
        profile_form = ProfileForm(request.POST or None, request.FILES or None)
        if user_form.is_valid() and profile_form.is_valid():
            # langageuser = Profile.objects.get(user=request.user)
            # langages = langageuser.langages.all()
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            print(user)
            profile = profile_form.save(commit=False)
            profile.user = user
            profile = profile.save()
            # print(langages)
            #grp_personnel = Group.objects.get_or_create(name='PERSONNEL')
            #grp_personnel[0].user_set.add(user)
            messages.success(request, "Profile Créé avec Succès")
            #return redirect('abonnes:add_profile')
            return redirect(reverse('params:add_profile'))
    else:
        user_form = UserRegistration()
        profile_form = ProfileForm()
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'abonnes/add_profile.html', context)

# Create your views here.
