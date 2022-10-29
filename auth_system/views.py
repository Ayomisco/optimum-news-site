from multiprocessing import context
# import profile
from django.shortcuts import redirect, render, get_object_or_404

# Authentication module
from auth_system.forms import ChangePasswordForm, SignupForm, EditProfileForm

from django.contrib.auth.models import User

# template loader
from django.template import loader

from django.http import HttpResponse

# importing decorator for login require
from django.contrib.auth.decorators import login_required

# clearing session and updating with a new one when password is reset
from django.contrib.auth import update_session_auth_hash

# Changing profile
from auth_system.models import *


from post.models import *

# Paginator Importation
from django.core.paginator import Paginator


# Create your views here.
# PROFILE VIEWS

def UserProfile(request, username):
    user = User.objects.get(username=username)
    # user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)

    # profile = Profile.objects.get(user=user)
    articles = profile.favourites.all()

    categories = Category.objects.all()
    tags = Tag.objects.all()


 # Paginator Starts here
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    articles_paginator = paginator.get_page(page_number)


    template = loader.get_template('user-profile.html')
    
    context = {
        'articles': articles_paginator,
        'profile': profile,
        'categories': categories,
        'tags': tags,
    }

    return HttpResponse(template.render(context, request))



# def Profile(request):
#     return render(request, 'user-profile.html')



def Signup(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            User.objects.create_user(username=username, email=email, password=password)
            return redirect('index')

    else:
        form = SignupForm()


    template = loader.get_template('signup.html')

    context = {
        'form': form,
        'categories': categories,
        'tags': tags,
    }

    # return render(request, 'signup.html', context)
    return HttpResponse(template.render(context, request))

@login_required
# CHange Password View
def ChangePassword(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('passwordresetsuccess')

    else:
        form = ChangePasswordForm(instance=user)
    
    context = {
        'form': form,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'change-password.html', context)

# Password reset success
def PasswordResetSuccess(request):
    return render(request, 'password_change_success.html')


@login_required
# Updating Profile View
def EditProfile(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    user = request.user.id
    profile = Profile.objects.get(user__id=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile.profile_pic = form.cleaned_data.get('profile_pic')
            profile.profile_banner = form.cleaned_data.get('profile_banner')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.url = form.cleaned_data.get('url')
            profile.profile_info = form.cleaned_data.get('profile_info')

            profile.save()
            # update_session_auth_hash(request, user)
            return redirect('index')

    else:
        form = EditProfileForm()

    context = {
        'form': form,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'edit_profile.html', context)

# Password reset success


# def PasswordResetSuccess(request):
#     return render(request, 'password_change_success.html')
