"""
Django settings for iop_sample project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u6jxrq9-sw99+zneusby0xh=ojpi!d5xe5a%j77)1g)3vl!#hk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'iop_sample.urls'

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

WSGI_APPLICATION = 'iop_sample.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")

MAIL_CONTENT = {
    'TEST_MAIL': {
        'SUBJECT': 'サンプルアプリ テストメール',
        'MESSAGE': 'テストメールです。'
    },
    "FUEL_ORDER_MAIL": {
        "SUBJECT": "燃料発注依頼",
        "MESSAGE": """<p>{ja_branch_office_name} 燃料担当者様</p>
        <p>下記依頼内容で燃料の発注をお願いいたします。</p>
        <br>
        <p>【依頼日時】{order_date}</p>
        <p>【依頼者】{user_id}</p>
        <p>【届け先ハウス】{farm_field_name}</p>
        <p>【燃料種類】{fuel_type}</p>
        <p>【数量】{quantity}L</p>
        <br>
        <p>依頼を確認した場合は、空メールで返信ください。</p>
        """
    },
    "CANCEL_FUEL_ORDER_MAIL": {
        "SUBJECT": "燃料発注キャンセル依頼",
        "MESSAGE": """<p>{ja_branch_office_name} 燃料担当者様</p>
        <p>下記依頼内容で依頼した燃料発注のキャンセルをお願いいたします。</p>
        <br>
        <p>【依頼日時】{order_date}</p>
        <p>【依頼者】{user_id}</p>
        <p>【届け先ハウス】{farm_field_name}</p>
        <p>【燃料種類】{fuel_type}</p>
        <p>【数量】{quantity}L</p>
        <br>
        <p>キャンセル依頼を確認した場合は、空メールで返信ください。</p>
        """
    }
}
