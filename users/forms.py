from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField()
    birth_date = forms.DateField()
    first_name= forms.CharField()
    last_name= forms.CharField()
    gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES, widget= forms.RadioSelect)
    
    class Meta:
        model= CustomUser
        fields=('first_name','last_name','email' ,'username','birth_date','gender','password1','password2')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model= CustomUser
        fields=['bio','profile_image','location',]