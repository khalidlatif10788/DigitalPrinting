from allauth.account.forms import SignupForm, LoginForm,UserForm
from django import forms
from django.contrib.auth.models import Group,User
#from online_retailer.models import customer

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_staff = True
        user.is_active = True
        user.save()
    
        return user

class CustomLoginForm(LoginForm):

    remember = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        