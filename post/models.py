
from pyexpat import model
from tabnanny import verbose
from django.db import models
# 
from django.urls import reverse

# Importing CKEDITOR
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('published', "Published"),
]


class Category(models.Model):
    title = models.CharField(max_length=112, verbose_name='Title')
    slug = models.SlugField(max_length=150, unique=True)


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('categories', args={self.slug})

    
class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Tag')
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

# Getting the slug Url
    def get_absolute_url(self):
        return reverse('tags', args={self.slug})



class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(unique=True)
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=10, verbose_name='status')
    publication_date = models.DateTimeField(verbose_name='Created')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    picture = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True, verbose_name='Picture')
    content = RichTextUploadingField(verbose_name="Content")
    author = models.CharField(max_length=30, default='Anonymous', verbose_name="Author")
    tags = models.ManyToManyField(Tag)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"
        

    class Meta:
        ordering = ['-publication_date']
        verbose_name = "Post"
        verbose_name_plural = "Posts"


# Getting the Post Url

    def get_absolute_url(self):
        return reverse('articledetails', args={self.slug})

# Contact Form Model
class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name='name')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=150, verbose_name='Subject')
    message_date = models.DateField( verbose_name='Message Date')
    message = models.TextField(max_length=3000)

    def __str__(self):
        return f"{self.name}, {self.email}"

    class Meta:
        ordering = ['-message_date']
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


# Changepassword
# class ChangePasswordForm()
