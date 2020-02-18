import os
import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['ALLOWED HOSTS HERE']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main.apps.MainConfig',
    'login.apps.LoginConfig',

    # social allauth apps
    'django.contrib.sites',       
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.linkedin',

    'pwa',
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

ROOT_URLCONF = 'myapp.urls'

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

WSGI_APPLICATION = 'myapp.wsgi.application'

# SQLite Database used for developement
#
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}
DATABASES = {
       'default': {
               'ENGINE': 'django.db.backends.mysql',
               'OPTIONS': {
                       'read_default_file': '/etc/mysql.cnf'
               },
       }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = (
    # this is the default authentication that we can extend - BUT WE MUST INCLUDE IT HERE
    'django.contrib.auth.backends.ModelBackend',
    
    # This is the allauth specific settings for authentication
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

LOGIN_URL = 'login-signin'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_LOGOUT_ON_GET = True

# PWA settings
PWA_APP_DEBUG_MODE = False

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'main/static/js', 'serviceworker.js')
PWA_APP_NAME = 'KnowLineCoffee'
PWA_APP_DESCRIPTION = 'Know the wait before you wait'
PWA_APP_THEME_COLOR = '#53b796'
PWA_APP_BACKGROUND_COLOR = '#53b796'
PWA_APP_ORIENTATION = 'portrait'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_START_URL = '/'
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

PWA_APP_ICONS = [ 
    {
        'src': '/static/images/icons/icon-72x72.png',
        'sizes': '72x72'
    },    
    {
        'src': '/static/images/icons/icon-96x96.png',
        'sizes': '96x96'
    },    
    {
        'src': '/static/images/icons/icon-128x128.png',
        'sizes': '128x128'
    },    
    {
        'src': '/static/images/icons/icon-144x144.png',
        'sizes': '144x144'
    },    
    {
        'src': '/static/images/icons/icon-152x152.png',
        'sizes': '152x152'
    },    
    {
        'src': '/static/images/icons/icon-192x192.png',
        'sizes': '192x192'
    },    
    {
        'src': '/static/images/icons/icon-384x384.png',
        'sizes': '384x384'
    },    
    {
        'src': '/static/images/icons/icon-512x512.png',
        'sizes': '512x512'
    },
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/icons/splash-200x300.png',
        'media': '(device-width: 200px) and (device-height: 300px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)' ,
    }, 
    {
        'src': '/static/images/icons/splash-320x426.png',
        'media': '(device-width: 320px) and (device-height: 426px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)' ,
    }, 
    {
        'src': '/static/images/icons/splash-320x470.png',
        'media': '(device-width: 320px) and (device-height: 470x) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)' ,
    }, 
    {
        'src': '/static/images/icons/splash-320x480.png',
        'media': '(device-width: 320px) and (device-height: 480x) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)' ,
    }, 
    {
        'src': '/static/images/icons/splash-426x320.png',
        'media': '(device-width: 426px) and (device-height: 320x) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)' ,
    }, 
    {
        'src': '/static/images/icons/splash-470x320.png',
        'media': '(device-width: 470px) and (device-height: 320x) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)' ,
    }, 
    {
        'src': '/static/images/icons/splash-480x640.png',
        'media': '(device-width: 480px) and (device-height: 640x) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)' ,
    }, 
    {
        'src': '/static/images/icons/splash-480x800.png',
        'media': '(device-width: 480px) and (device-height: 800x) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)' ,
    }, 
    {
        'src': '/static/images/icons/splash-620x300.png',
        'media': '(device-width: 620px) and (device-height: 300x) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)' ,
    }, 
    {
        'src': '/static/images/icons/splash-640x680.png',
        'media': '(device-width: 640px) and (device-height: 680x) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)' ,
    }, 
    {
        'src': '/static/images/icons/splash-640x960.png',
        'media': '(device-width: 640px) and (device-height: 960x) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)' ,
    }, 
    {
        'src': '/static/images/icons/splash-640x1136.png',
        'media': '(device-width: 640px) and (device-height: 1136px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)' ,
    }, 
    {
        'src': '/static/images/icons/splash-720x960.png',
        'media': '(device-width: 720px) and (device-height: 960px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)',
    }, 
    {
        'src': '/static/images/icons/splash-750x1294.png',
        'media': '(device-width: 750px) and (device-height: 1294px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)',
    }, 
    {
        'src': '/static/images/icons/splash-750x1334.png',
        'media': '(device-width: 750px) and (device-height: 1334px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)',
    }, 
    {
        'src': '/static/images/icons/splash-768x1024.png',
        'media': '(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)',
    },  
    {
        'src': '/static/images/icons/splash-828x1792.png',
        'media': '(device-width: 898px) and (device-height: 1792px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)',
    }, 
    {
        'src': '/static/images/icons/splash-960x720.png',
        'media': '(device-width: 960px) and (device-height: 720px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)',
    }, 
    {
        'src': '/static/images/icons/splash-1024x768.png',
        'media': '(device-width: 1024px) and (device-height: 768px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)',
    }, 
    {
        'src': '/static/images/icons/splash-1125x2436.png',
        'media': '(device-width: 1125px) and (device-height: 2436px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)',
    }, 
    {
        'src': '/static/images/icons/splash-1152x1920.png',
        'media': '(device-width: 1152px) and (device-height: 1920px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)',
    },  
    {
        'src': '/static/images/icons/splash-1242x2148.png',
        'media': '(device-width: 1242px) and (device-height: 2148px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)',
    }, 
    {
        'src': '/static/images/icons/splash-1242x2208.png',
        'media': '(device-width: 1242px) and (device-height: 2208px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)',
    }, 
    {
        'src': '/static/images/icons/splash-1242x2688.png',
        'media': '(device-width: 1242px) and (device-height: 2688px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)',
    }, 
    {
        'src': '/static/images/icons/splash-1536x2048.png',
        'media': '(device-width: 1536px) and (device-height: 2048px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)',
    }, 
    {
        'src': '/static/images/icons/splash-1668x2224.png',
        'media': '(device-width: 1668px) and (device-height: 2224px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)',
    }, 
    {
        'src': '/static/images/icons/splash-1668x2388.png',
        'media': '(device-width: 1668px) and (device-height: 2388px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)',
    }, 
    {
        'src': '/static/images/icons/splash-2048x1536.png',
        'media': '(device-width: 2048px) and (device-height: 1536px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)',
    }, 
    {
        'src': '/static/images/icons/splash-2048x2732.png',
        'media': '(min-device-width: 2048px) and (max-device-width: 2732px) and (-webkit-min-device-pixel-ratio: 2) and (orientation: portrait)',
    }, 
    {
        'src': '/static/images/icons/splash-2208x1242.png',
        'media': '(min-device-width: 2208px) and (max-device-width: 1242px) and (-webkit-min-device-pixel-ratio: 2) and (orientation: portrait)',
    }
]