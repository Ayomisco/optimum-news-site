from django.urls import path
from post.views import *

urlpatterns = [
    path('', index, name='index'),
    path('categories/<slug:category_slug>', category, name='categories'),
    path('tags/<slug:tag_slug>', tags, name='tags'),
    path('<slug:post_slug>', PostDetails, name='articledetails'),
    path('contact/', Contact, name='contact'),
    path('contact/success/', Contactsuccess, name='contactsuccess'),

]