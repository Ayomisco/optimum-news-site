from dataclasses import field, fields
from email import message
import re
from django import forms

from django.contrib.auth.models import User

from auth_system.models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Validation modules
from django.core.exceptions import ValidationError
from django.contrib import messages

# Formbidden Usernames
def ForbiddenUsers(value):
    forbidden_users = ['admin', 'css', 'js', 'authenticate', 'login', 'master', 'administrator', 
    'root', 'email', 'user', 'join', 'static', 'python']

    if value.lower() in forbidden_users:
        raise ValidationError("This is a reserve word.")


def InvalidUser(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError("This is an invalid user, Do not use any of these chars: @, -, +")


def UniqueEmail(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this email already exists.')


def UniqueUsername(value):
    if User.objects.filter(username__iexact=value).exists:
        raise ValidationError('User with this Username already exists.')



# Setting the input field
class SignupForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(), max_length=30, required=True)
    email = forms.CharField(
        widget=forms.EmailInput(), max_length=100, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(), required=True)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(), required=True)




    class Meta:
        model = User
        # message = forms.CharField(widget=CKEditorUploadingWidget())
        fields = ( 'email', 'username', 'password')

    # Maching the validation with the form input
    def __ini__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(ForbiddenUsers)
        self.fields['username'].validators.append(InvalidUser)
        self.fields['username'].validators.append(UniqueUsername)
        self.fields['email'].validators.append(UniqueEmail)

    def clean(self):
        super(SignupForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        # overiding the clean function to make sure password is validate
        if password != confirm_password:
            self._errors['password'] = self.error_class(['Password do not match, try again!'])

        return self.cleaned_data

# Change Password form
class ChangePasswordForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    old_password = forms.CharField(widget=forms.PasswordInput(), label="Old Password", required=True)
    new_password = forms.CharField(
        widget=forms.PasswordInput(), label="New Password", required=True)

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(), label="Confirm new Password", required=True)

    class Meta:
        model = User
        fields = ['id', 'old_password', 'new_password', 'confirm_password']

    def clean(self):
        super(ChangePasswordForm, self).clean()
        id = self.cleaned_data.get('id')
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')

        user = User.objects.get(pk=id)
        if new_password != confirm_password:
            self._errors['new_password'] = self.error_class(
                ['Password do not match, try again!'])

        if not user.check_password(old_password):
            self._errors['old_password'] = self.error_class(['Old Password do not match'])

        

        return self.cleaned_data


class EditProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=False)
    profile_banner = forms.ImageField(required=False)
    first_name = forms.CharField(
        widget=forms.TextInput(), max_length=50, required=False)
    last_name = forms.CharField(
        widget=forms.TextInput(), max_length=50, required=False)
    location = forms.CharField(
        widget=forms.TextInput(), max_length=25, required=False)
    url = forms.URLField(
        widget=forms.TextInput(), max_length=200, required=False)
    profile_info = forms.CharField(
        widget=forms.TextInput(), max_length=400, required=False)

    class Meta:
        model = Profile
        fields = ('profile_pic', 'first_name', 'last_name',
                  'location', 'url', 'profile_info')
