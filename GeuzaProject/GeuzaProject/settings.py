"""
Django settings for GeuzaProject project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""




import  os
from pathlib import Path
import subprocess
#from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vox)=z)5w5m64t0lqi35^j5amseo^b6vof8cc129e#ge4*f6$*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    #'admin_tools_stats',
    'jazzmin',
    'django_nvd3',
    # 'adminlte3',
    # 'adminlte3_theme',
    'django_static_fontawesome',
    'django_static_jquery3',
    #'django_admin_global_sidebar',
    # "admin_interface",
    "colorfield",
    'django_light',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    #'admin_user',
    'django.contrib.contenttypes',
    #'adminlte_helpers',
    #'mapbox_location_field',
    'djangobower',
    #'maps',
    # 'django_google_maps',
    # 'geopy',
    # 'djangoflutterwave',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'user.middleware.VisitorMiddleware',
    'user.middleware.TrafficLoggingMiddleware',

]

ROOT_URLCONF = 'djangoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), ]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #'adminlte_helpers.context_processors.adminlte',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# GDAL_LIBRARY_PATH = r'C:\OSGeo4W\bin\ogrinfo.exe'
# subprocess.run([GDAL_LIBRARY_PATH, '--version'])
# MAPBOX_KEY = 'sk.eyJ1IjoiYnJpYW5heXQiLCJhIjoiY2xwNzllaWhmMmI4MDJpcnBvdmU1eTF0YiJ9.RODaGeDAVMdyqSOTcyLlQg'
# LOCATION_FIELD_PROVIDER = 'mapbox'
ADMIN_CHARTS_NVD3_JS_PATH = 'bow/nvd3/build/nv.d3.js'
ADMIN_CHARTS_NVD3_CSS_PATH = 'bow/nvd3/build/nv.d3.css'
ADMIN_CHARTS_D3_JS_PATH = 'bow/d3/d3.js'

BOWER_INSTALLED_APPS = (
    'd3#3.3.13',
    'nvd3#1.8.6',
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
X_FRAME_OPTIONS = 'SAMEORIGIN'              # allows you to use modals insated of popups
SILENCED_SYSTEM_CHECKS = ["security.W019"]
# MAPBOX_GEOCODING_API_URL = 'https://api.mapbox.com/geocoding/v5/mapbox.places/{query}.json'
# os.environ['GDAL_DATA'] = '/OSGeo4W/bin'
# os.environ['PROJ_LIB'] = '/Users/AYT-BRAIN/PY'
GOOGLE_MAPS_API_KEY = 'AIzaSyAkp4_XGKzx8Xy5R7R5AYA-QCKt139LCjE'
LOCATION_FIELD_GOOGLE_MAPS_API_KEY = 'AIzaSyAkp4_XGKzx8Xy5R7R5AYA-QCKt139LCjE'

LOCATION_FIELD = {
   'map.provider': 'google',
   'map.zoom': 13,
   'search.provider': 'google',
   'search.suffix': '',
   'map.api_key':  'AIzaSyAkp4_XGKzx8Xy5R7R5AYA-QCKt139LCjE',
}

FLW_PRODUCTION_PUBLIC_KEY = "FLWPUBK_TEST-9e8554a09dda21a024d85a6227f0d62b-X"
FLW_PRODUCTION_SECRET_KEY = "FLWSECK_TEST-5564f194ad78842c12a0016c94447fc0-X"
FLW_SANDBOX_PUBLIC_KEY = "FLWPUBK_TEST-9e8554a09dda21a024d85a6227f0d62b-X"
FLW_SANDBOX_SECRET_KEY = "FLWSECK_TEST-5564f194ad78842c12a0016c94447fc0-X"
FLW_SANDBOX = True

JAZZMIN_SETTINGS = {
    "site_title": "GEUZA ",
    "site_header": "GEUZA ",
    "site_brand": " GEUZA ",
    "site_logo": "/images/fav_g1.png",  # Path to your custom logo
    "welcome_sign": "Welcome to GEUZA ",
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # Add more links here
    ],
    "usermenu_links": [
        {"name": "Support", "url": "https://support.example.com", "new_window": True},
        # Add more user menu links here
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "copyright": "GEUZA @2024",
    "login_logo": "/images/GEUZA.png",
    "welcome_sign": "Welcome to GEUZA admin",
    "changeform_format": "single",

    # More configurations can be added here
}
JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",  # or any other theme you selected
    "button_classes": {
        "primary": "btn btn-primary-custom",
        "secondary": "btn btn-secondary-custom",
        "info": "btn btn-info-custom",
        "warning": "btn btn-warning-custom",
        "danger": "btn btn-danger-custom",
        "success": "btn btn-success-custom"
    },
    "show_ui_builder": True,
}
# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'geuzzaministries@gmail.com'
EMAIL_HOST_PASSWORD = "#geuza256"
DEFAULT_FROM_EMAIL = 'geuzzaministries@gmail.com'

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

