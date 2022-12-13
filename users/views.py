from django.http import HttpResponseRedirect
from django.shortcuts import render
from allauth.account.views import SignupView, LoginView
from users.forms import CustomSignupForm, CustomLoginForm
from django.urls import reverse_lazy


# Create your views here.


class CustoomloginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'accounts/login.html'
    success_url = None
    redirect_field_name = "next"
   
   # success_url=


class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    template_name = 'accounts/register.html'
    
    #success_url = reverse_lazy('login')


def index(request):
    return render(request, 'home/index.html', {"":""})