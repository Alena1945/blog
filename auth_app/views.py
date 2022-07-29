from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm


class LogInView(View):
    def get(self, request):
        return render(request, 'auth_app/login.html')

    def post(self, request):
        # print(request.POST)
        form = LoginForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'auth_app/login.html', status=400)
        login(request, user=form.cleaned_data['user'])
        return render(request, 'blog/index.html')


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class SignUpView(View):
    def get(self, request):
        return render(request, 'auth_app/sign_up.html')



