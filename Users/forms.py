from django import forms
from django.core.exceptions import ValidationError

from Users.models import User


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'گذرواژه'}))


class UserRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'گذرواژه'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'تکرار گذرواژه'}))

    def clean_email(self):
        data = self.cleaned_data['email']
        user = User.objects.filter(email=data).exists()
        if user:
            raise ValidationError('این ایمیل از قبل ثبت شده است ، با یک ایمیل دیگری امتحان کنید')

        return data

    def clean_confirm_password(self):
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['confirm_password']

        if pass1 != pass2:
            raise ValidationError('گذرواژه ها با یکدیگر مطابقت ندارند')

        return pass2