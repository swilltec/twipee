"""
Django settings for development project.
"""
from .base import *

DEBUG = True
SECRET_KEY = 'django-insecure-idzx47o)bw0d57e3##dq@yd@dakge))3=t0r+h!3%++)ub*e5r'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'