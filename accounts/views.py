from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signUp(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username,
                                password=request.POST['password1'],
                                email=user.email,
                                first_name=user.first_name,
                                last_name=user.last_name)
            login(request, user)
            return redirect('/login')

    return render(request, 'registration/signup.html', {'form':  form})
