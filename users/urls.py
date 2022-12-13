from django.urls import path, include
from allauth.account.views import LogoutView
from .views import CustomSignupView, CustoomloginView, index



urlpatterns = [
    # path('', index, name=''),
    path('home' , index, name='home'),
    path('signup/' ,CustomSignupView.as_view(), name='signup-user'),
    path('login/' ,CustoomloginView.as_view(), name='login-user'),
    path('logout/' ,LogoutView.as_view(),name='logout'),
]
app_name = 'users'