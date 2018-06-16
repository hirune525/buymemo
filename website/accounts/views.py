from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import LoginForm


class LoginView(View):

    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        ''' ログイン画面の表示 '''
        context = {
            'form': LoginForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        ''' ログイン認証 '''
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        user = form.user

        auth_login(request, user)

        return redirect(reverse('buymemo:index'))


class LogoutView(View):

    template_name = 'accounts/logout.html'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return render(request, self.template_name)
