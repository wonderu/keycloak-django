"""
Django settings for keycloak_example project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
import json
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "django-insecure-jd80ri@esgssrj3acs$to$x462#m^806732ugam&+tb_u$fbe&"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0", "*"]


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of allauth
    # 'django.contrib.auth.backends.ModelBackend',
    # allauth specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth_keycloak_ext",
    "start",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "keycloak_example.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR.joinpath("templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "keycloak_example.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("SQL_DATABASE", "app"),
        "USER": os.environ.get("SQL_USER", "app_user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "app_password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5445"),
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SITE_ID = 1


def getGroups():
    groups = os.environ.get(
        "KEYCLOAK_GROUPS",
        {
            "GROUP_TO_FLAG_MAPPING": {
                "is_staff": ["Django Staff", "django-admin-role"],
                "is_superuser": "django-admin-role",
            },
            "GROUPS_MAPPING": {
                # "django-admin-role": "django-admin-group",
                "django-admin-role": None,
                "offline_access": None,
            },
            "GROUPS_AUTO_CREATE": True,
        },
    )

    print(groups)

    if isinstance(groups, str):
        groups = json.loads(groups)

    return groups


# Set your keycloak url and realm
SOCIALACCOUNT_PROVIDERS = {
    "keycloak_ext": {
        "APP": {
            "client_id": os.environ.get("KEYCLOAK_CLIENT_ID", "django-allauth"),
            "secret": os.environ.get(
                "KEYCLOAK_SECRET", "B5JcyEVyyHrRoMIsmopCwYrBW5QFsdu2"
            ),
            "key": "",
        },
        "KEYCLOAK_URL": os.environ.get("KEYCLOAK_URL", "http://keycloak:8080"),
        # "KEYCLOAK_URL_ALT": "http://keycloak:8080",
        "KEYCLOAK_REALM": os.environ.get("KEYCLOAK_REALM", "master"),
        "GROUPS": getGroups(),
    }
}

# ACCOUNT_ADAPTER = "start.adapter.NoNewUsersAccountAdapter"
# SOCIALACCOUNT_ADAPTER = "start.adapter.SocialAccountAdapter"

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
