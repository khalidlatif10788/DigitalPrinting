"""
Django settings for RoseColorLab project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from django.urls import reverse_lazy, reverse
from django.core.management.utils import get_random_secret_key
import sys
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ['secrect-k'] 
#SECRET_KEY="django-insecure-x9auh99*f_gm70*x5#w_tmc0@vj#zpte)(5wb$-&!e!r*oj4^6"
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = os.getenv("DEBUG", "False") == "True"
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"
#ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
ALLOWED_HOSTS = ["*"]
# ALLOWED_HOSTS = ['localhost','127.0.0.1']
# ALLOWED_HOSTS = ["rosecolor.herokuapp.com","localhost"]
# CSRF_TRUSTED_ORIGINS = ["https://rosecolor.herokuapp.com"]

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DigitalPrintingPress',
    'django_admin_generator',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    #  'allauth.socialaccount.providers.twitter',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT_URLCONF = 'RoseColorLab.urls'
# TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                     # `allauth` needs this from django
                'django.template.context_processors.request',
                
            ],
        }
    },
]

WSGI_APPLICATION = 'RoseColorLab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
if DEVELOPMENT_MODE is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Karachi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets') 

# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'static'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


ACCOUNT_FORMS = {
    # 'login': 'DigitalPrintingPress.form.CustomLoginForm',
    # 'signup':'DigitalPrintingPress.form.CustomSignupForm',
    # 'add_email': 'DigitalPrintingPress.form.MyCustomAddEmailForm',
    # 'change_password': 'DigitalPrintingPress.form.MyCustomChangePasswordForm',
    # 'set_password': 'DigitalPrintingPress.form.MyCustomSetPasswordForm',
    # 'reset_password': 'DigitalPrintingPress.form.MyCustomResetPasswordForm',
    # 'reset_password_from_key': 'DigitalPrintingPress.form.MyCustomResetPasswordKeyForm',
    'login': 'allauth.account.forms.LoginForm',
    'signup': 'allauth.account.forms.SignupForm',
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
    
    
}
ROOT_URLCONF = 'RoseColorLab.urls'
# LOGIN_REDIRECT_URL = reverse_lazy('categoryList')
# LOGIN_URL = reverse_lazy('users:login-user')
# LOGOUT_REDIRECT_URL =('users:login-user')

# STATIC_URL = 'static/'
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# LOGIN_REDIRECT_URL='/profile-order/' alauth change

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
LOGIN_URL = 'accounts/login'
# LOGOUT_URL = 'DigitalPrintingPress/login/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True #new

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

LOGIN_REDIRECT_URL = '/'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #new
EMAIL_HOST = 'smtp.gmail.com' #new
EMAIL_PORT = 587 #new
EMAIL_HOST_USER = 'realism10788@gmail.com'  #new
EMAIL_HOST_PASSWORD = "zizpescoubguzhaa"#new
EMAIL_USE_TLS = True #new
