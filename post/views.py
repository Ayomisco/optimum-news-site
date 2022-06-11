from multiprocessing import context

from re import template
from django.shortcuts import redirect, render, get_object_or_404, render
from django.http import HttpResponse
from django.contrib import messages

# Modules
from django.template import loader

# Models
from post.models import *
from auth_system.models import *
# Django Shortcuts

# Importing form
from post.forms import ContactForm

#importing django timezone from utils
from django.utils import timezone

# Paginator Importation
from django.core.paginator import Paginator

# Importing queryset
from django.db.models import Q

# Create your views here.

def index(request):
    # articles = Post.objects.all()
    articles = Post.objects.filter(status='published').order_by('-publication_date')
    categories = Category.objects.all()
    tags = Tag.objects.all()


    # Search Query
    query = request.GET.get("q")
    # query = request.GET['q']
    if query:
        articles = articles.filter(
            Q(title__icontains=query)|
            # distinct will remove every duplicated articles
            Q(content__icontains=query)).distinct()

    # Paginator Starts here
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    articles_paginator = paginator.get_page(page_number)

    template = loader.get_template('index.html')

    context = {
        'articles': articles_paginator,
        'categories': categories,
        'tags': tags
    }

    return HttpResponse(template.render(context, request))


def tags(request, tag_slug):

    articles = Post.objects.filter(
        status='published').order_by('-publication_date')
    tags = Tag.objects.all()
    categories = Category.objects.all()

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        articles = articles.filter(tags=tag)

    # Search Query
    query = request.GET.get("q")
    # query = request.GET['q']
    if query:
        articles = articles.filter(
            Q(title__icontains=query) |
            # distinct will remove every duplicated articles
            Q(content__icontains=query)).distinct()

    # Paginattion Starts Here
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    categories_paginator = paginator.get_page(page_number)

    
    template = loader.get_template('tags.html')

    context = {
        'articles': categories_paginator,
        'categories': categories,
        'tags': tags,
    }

    return HttpResponse(template.render(context, request))



def category(request, category_slug):
    articles = Post.objects.filter(status='published').order_by('-publication_date')
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        articles = articles.filter(category=category)

    

    template = loader.get_template('category.html')
    
    context = {
        'articles': articles,
        'categories': categories,
        'tags': tags
    }

    return HttpResponse(template.render(context, request))


# articles = Post.objects.filter(
#     status='published').order_by('-publication_date')

#    if tag_slug:

#         tag = get_object_or_404(Tag, slug=tag_slug)
#         articles = articles.filter(tags=tag)

#     context = {
#         'articles': articles,
#         'tags': tags,

#     }
#     return HttpResponse(template.render(context, request))




# Post Detail Start Here
def PostDetails(request, post_slug):
    article = get_object_or_404(Post, slug=post_slug)

    tags = Tag.objects.all()
    categories = Category.objects.all()
    # getting favourite post
    user = request.user.id
    
    profile = Profile.objects.get(user__id=user)

    # Favourite button colour changing
    if profile.favourites.filter(slug=post_slug).exists():
        favourited = True
    else:
        favourited = False

    
# Handle the post to add uder's favourite article
    if request.method == 'POST':
        if profile.favourites.filter(slug=post_slug).exists():
            profile.favourites.remove(article)
        else:
            profile.favourites.add(article)
        

    template = loader.get_template('post-detail.html')

    context = {
        'article':article,
        'favourited': favourited,
        'categories': categories,
        'tags': tags
    }
    
    return HttpResponse(template.render(context, request))


# Contact Form Start Here
def Contact(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            # saving it base on timezone
            message.message_date = timezone.now()
            form.save()
            messages.success(request, 'Your profile is updated successfully!')

            return redirect('contactsuccess')
    
    else:
        form = ContactForm()

    context = {
        'form': form,
        'categories': categories,
        'tags': tags
    }

    return render(request, 'contact.html', context)

# Static website for the form contact
def Contactsuccess(request):
    return render(request, 'contactsuccess.html')