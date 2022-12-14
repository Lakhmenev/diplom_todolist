"""
Django settings for todolist project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from typing import Any

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_DIR = environ.Path(__file__) - 3


# Take environment variables from .env file
# environ.Env.read_env(BASE_DIR.joinpath('.env'))
environ.Env.read_env(ROOT_DIR + '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', False)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'social_django',
    'core',
    'goals',
    'bot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'todolist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'todolist.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': 'todolist.db',
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': env.str('POSTGRES_HOST', default='127.0.0.1'),
        'PORT': env.int('POSTGRES_PORT', 5432),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'  # "en-us"

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'core.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR.parent.joinpath('deploy', 'nginx', 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend', ]
}

LOGGING: dict[str, Any] = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'health-check': {
            '()': 'todolist.filters.HealthCheckFilter',
        },
    },
    'formatters': {
        'console': {
            'format': '%(asctime)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m--%d %H:%M:%S',
        },
        'sample': {
            'format': '%(asctime)s - %(levelname)s - %(module)s - %(message)s',
            'datefmt': '%Y-%m--%d %H:%M:%S',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['health-check'],
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        'project': {
            'level': 'DEBUG',
            'filters': ['health-check'],
            'class': 'logging.StreamHandler',
            'formatter': 'sample',
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'handlers': ['project'],
        },
        'django.server': {
            'level': 'INFO',
            'handlers': ['console'],
        },
    }
}

if env.bool('SQL_ECHO', False):
    LOGGING['loggers'].update({
        'django.db': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False
        }
    })

SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_VK_OAUTH2_KEY = env.str('VK_OAUTH2_KEY')
SOCIAL_AUTH_VK_OAUTH2_SECRET = env.str('VK_OAUTH2_SECRET')

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']
SOCIAL_AUTH_VK_EXTRA_DATA = [('email', 'email')]

# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/logged-in/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'

BOT_TOKEN = env.str('BOT_TOKEN', default='')

AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',  # ?????????????????????? ?????????? ??????????????????
    'django.contrib.auth.backends.ModelBackend',
    # ???????????????????????? ????????????????????????????, ?????? ???????????? ?????????????????????? ?????????? ?????????????? ?????????? ?? ????????????
)
