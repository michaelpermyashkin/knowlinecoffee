from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from login.forms import SignUpForm, UsersLoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main-home')
    else:
        form = SignUpForm()
    return render(request, 'login/signup.html', {'form': form})

def signin(request):
    print(request.GET.get('next'))
    form = UsersLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        login(request, user)
        
        next_url = request.GET.get('next')
        if next_url:
            return redirect(next_url)
        else:
            return render(request, 'main-home')
    return render(request, "login/login.html", {"form" : form})

def signout(request):
    return render(request, 'login/signout.html')
    
