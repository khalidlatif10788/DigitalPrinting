# dataclasses import field
from dataclasses import fields
from django import forms
from django.contrib import admin

from allauth.account.forms import SignupForm, LoginForm,AddEmailForm,ChangePasswordForm,SetPasswordForm,ResetPasswordForm,ResetPasswordKeyForm
from django import forms
from django.contrib.auth.models import Group,User
from django.forms import ModelForm
from DigitalPrintingPress.models import adress,SubCategory
from.models import Product,MainCategoery,SubCategory
from django.db import models


#from online_retailer.models import customer

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        User.first_name = self.cleaned_data['first_name']
        User.last_name = self.cleaned_data['last_name']
        User.is_staff = False
        User.is_active = True
        user.save()
    
        return user

class CustomLoginForm(LoginForm):

    remember = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

class MyCustomSetPasswordForm(SetPasswordForm):

    def save(self):

        # Ensure you call the parent class's save.
        # .save() does not return anything
        super(MyCustomSetPasswordForm, self).save()

        # Add your own processing here.
class MyCustomResetPasswordForm(ResetPasswordForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a string containing the email address supplied
        email_address = super(MyCustomResetPasswordForm, self).save(request)

        # Add your own processing here.

        # Ensure you return the original result
        return email_address
class AddressForm(ModelForm):
  class Meta:
        model = adress
        fields = ['shipping_address']

class MyCustomAddEmailForm(AddEmailForm):

    def save(self):

        # Ensure you call the parent class's save.
        # .save() returns an allauth.account.models.EmailAddress object.
        email_address_obj = super(MyCustomAddEmailForm, self).save()

        # Add your own processing here.

        # You must return the original result.
        return email_address_obj

class MyCustomChangePasswordForm(ChangePasswordForm):

    def save(self):

        # Ensure you call the parent class's save.
        # .save() does not return anything
        super(MyCustomChangePasswordForm, self).save()

        # Add your own processing here.
class MyCustomResetPasswordKeyForm(ResetPasswordKeyForm):

    def save(self):

        # Add your own processing here.

        # Ensure you call the parent class's save.
        # .save() does not return anything
        super(MyCustomResetPasswordKeyForm, self).save()
class productCustomForm(forms.ModelForm):
    # tuplist=[]
    
    class Meta:
        model = Product
        fields = '__all__'
        
    # def __init__(self, *args, **kwargs):
      
    #     super().__init__(*args, **kwargs)
    #     self.fields['product_sub_category_id'].queryset =SubCategory.objects.none()
    #     print('-----------------------------------------print data-----------------')
    #     print(self)
    #     print('-----------------------------------------print selfdata-----------------')
    #     main_id = self.data.get('main_category_id')
    #     print(main_id)
    #     if 'product_main_category_id' in self.data:
    #          main_id = int(self.data.get('product_main_category_id'))
    #          self.fields['product_sub_category_id'].queryset =SubCategory.objects. filter(sub_main_category_id=main_id)
      