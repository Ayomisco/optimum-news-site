from django.db import models
from django.contrib.auth.models import User
from post.models import Post
# 
from django.db.models.signals import pre_save, post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Username')
    first_name = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='First Name')
    last_name = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Last Name')

    location = models.CharField(max_length=50, null=True, blank=True, verbose_name='Location')
    url = models.URLField(max_length=80, null=True, blank=True)
    profile_info = models.TextField(max_length=250, null=True, blank=True, verbose_name='About Me')
    created_at = models.DateField(auto_now_add=True)
    favourites = models.ManyToManyField(Post, verbose_name='Favourite Article')
    profile_pic = models.ImageField(
        upload_to='profile_pictures', blank=True, verbose_name='Picture')
    profile_banner = models.ImageField(
        upload_to='profile_pictures', blank=True, verbose_name='Picture')
    

    def __str__(self):
        return f"{self.user}, {self.created_at}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
