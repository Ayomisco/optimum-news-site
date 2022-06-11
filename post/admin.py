from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


# class ContactAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ['status', 'tags']
    list_display = ['title', 'publication_date', 'category', 'author']


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Contact)




