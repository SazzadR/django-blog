from django.views import View
from django.urls import reverse
from djangounchained import settings
from django.http import HttpResponse
from accounts.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


class Login(View):
    def get(self, request):
        form = LoginForm()

        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

        return render(request, 'accounts/login.html', {'form': form})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('blog:home'))
