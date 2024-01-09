from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            form = AuthenticationForm()
            return render(request = request, template_name = "sizzlers/login.html", context={"form":form})
    else:
        form = AuthenticationForm()
    return render(request, 'sizzlers/login.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'sizzlers/login.html')
    else:
        form = UserCreationForm()
    return render(request, 'sizzlers/signup.html', {'form': form, 'submit_value': 'Sign Up'})


def home(request):
    return render(request, 'sizzlers/homepage.html')



