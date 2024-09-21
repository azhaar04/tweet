from django.shortcuts import render
from .forms import  UserRegistrationForm, UserProfileForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import CustomUser

# Create your views here.
def register(request):
    if request.method== 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form= UserRegistrationForm()


    return render(request, 'registration/register.html', {'form':form})


def user_profile(request):
    return render(request, 'user_profile.html')


@login_required
def profile_edit(request,user_id):
    user = get_object_or_404(CustomUser, pk= user_id)

    if user != request.user:
        return redirect('user_profile') 

    if request.method=='POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user= form.save(commit=False)
            
            user.save()
            return redirect('user_profile')    
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'user_profile_edit.html', {'form':form})