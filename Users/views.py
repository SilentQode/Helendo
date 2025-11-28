from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from Users.forms import *

from common.utils import validate_email


# Create your views here.


class UserLoginView(View):
    template_name = 'Users/login.html'
    form_class = UserLoginForm
    register_form_class = UserRegisterForm
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form_class, 'register_form': self.register_form_class})

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home:home')

            else:
                messages.error(request, 'اطلاعات کاربری صحیح نمی باشد', 'danger')
                return redirect('accounts:login')
        return render(request, self.template_name, context={'form': self.form_class})


class UserRegisterView(View):
    form_class = UserRegisterForm

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            result = validate_email(data['email'])
            if result:
                user = User.objects.create_user(username=data['username'], email=data['email'],
                                                password=data['password'])
                login(request, user)
                return redirect('home:home')
            else:
                messages.error(request, 'ایمیل شما صحیح نمی باشد', 'danger')
                return redirect('accounts:login')
        else:
            for error_list in form.errors.values():
                for error in error_list:
                    messages.error(request, error, 'danger')
            return redirect('accounts:login')