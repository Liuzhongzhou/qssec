# -*- coding: utf-8 -*-

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'beacon',
        'USER': 'root',
        'PASSWORD': 'root123',
        'HOST': '192.168.12.38',
        'PORT': '3306',
    }
}
