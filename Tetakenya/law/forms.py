from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Client, Lawyer, User, Service
from django.db import transaction


class ClientSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    Phone_Number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        client = Client.objects.create(user=user)
        client.first_name = self.cleaned_data.get('first_name')
        client.last_name = self.cleaned_data.get('last_name')
        client.email = self.cleaned_data.get('email')
        client.Phone_Number = self.cleaned_data.get('Phone_Number')
        client.save()
        return user


class LawyerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    county = forms.CharField(required=True)
    experience = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_lawyer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.county = self.cleaned_data.get('county')
        user.save()
        lawyer = Lawyer.objects.create(user=user)
        lawyer.first_name = self.cleaned_data.get('first_name')
        lawyer.county = self.cleaned_data.get('county')
        lawyer.experience = self.cleaned_data.get('experience')
        lawyer.save()
        return user


class LawyerUpdateForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = ['first_name', 'county', 'experience', 'profile_pic']
        exclude = ['user']


class UsernameUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
