from django.shortcuts import render

# Create your views here.
def signUp(request):
    return render(request,'registration/signup.html')