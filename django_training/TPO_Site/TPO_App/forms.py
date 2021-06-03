from django import forms
from django.contrib.auth.models import User
from TPO_App.models import UserInfoModel


class UserRegistrationModelForm(forms.ModelForm):
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        user_data = super().clean()
        if user_data['password'] != user_data['ConfirmPassword']:
            raise forms.ValidationError("Passwords did not match!")
        return user_data


class UserLoginModelForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['email','password']

class UserInfoModelForm(forms.ModelForm):
    class Meta():
        model = UserInfoModel
        fields = '__all__'