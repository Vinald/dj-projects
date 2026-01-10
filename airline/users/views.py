from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'users/user.html')


def login_view(request):
    next_url = request.POST.get('next') or request.GET.get('next') or reverse('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(next_url)
        else:
            return render(request, 'users/login.html', {'message': 'Invalid credentials', 'next': request.POST.get('next', '')})
    return render(request, 'users/login.html', {'next': request.GET.get('next', '')})


def logout_view(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('login'), {'message': 'Logged out successfully'})