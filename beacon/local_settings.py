# -*- coding: utf-8 -*-

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
import os
import settings

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

import djcelery

djcelery.setup_loader()
BROKER_URL = 'redis://:adminxxx@192.168.12.23:6379/15'
CELERY_RESULT_BACKEND = 'redis://:adminxxx@192.168.12.23:6379/15'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = settings.TIME_ZONE
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# 任务定义所在的模块
CELERY_IMPORTS = ('beacon_rpc.tasks',)

from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'test': {
        'task': 'beacon_rpc.tasks.test',
        'schedule': crontab(minute="*/1"),
        'args': ()
    },
    'app_list': {
        'task': 'beacon_rpc.tasks.app_list',
        'schedule': crontab(minute="*/1"),
        'args': ()
    }
}


LOG_DIR = './'
# LOG_DIR = 'E:/pywork/fort'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] [%(levelname)s] %(module)s %(process)d %(thread)d %(filename)s:%(lineno)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%[(asctime)s] [%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            # 'filters': ['special']
        },
        'beacon': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'beacon.log'),
            'formatter': 'verbose',
        },
        'beacon_user': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'beacon_user.log'),
            'formatter': 'verbose',
        },
        'beacon_rpc': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'beacon_rpc.log'),
            'formatter': 'verbose',
        },

    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'console': {
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'django.db': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'beacon': {
            'handlers': ['beacon', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'beacon_user': {
            'handlers': ['beacon_user', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'beacon_rpc': {
            'handlers': ['beacon_rpc', 'file'],
            'level': 'INFO',
            'propagate': True,
        },

    },
}
