from os import path

from backend.settings import config as c


# Main settings
SITE_ID                     = 1
NAME                        = c('name')
DEBUG                       = c('debug', default=False, cast=bool)
SECRET_KEY                  = c('secret-key')
INTERNAL_IPS                = c('internal-ips')
ALLOWED_HOSTS               = c('allowed-hosts')

SETTINGS_DIR                = path.dirname(path.dirname(path.abspath(__file__)))
BASE_DIR                    = path.dirname(SETTINGS_DIR)

ROOT_URLCONF                = 'backend.urls'
WSGI_APPLICATION            = 'backend.wsgi.application'
LOG_LEVEL                   = 'DEBUG' if DEBUG else 'INFO'
SCHEME                      = 'http' if DEBUG else 'https'
FQDN                        = ALLOWED_HOSTS[0]


# Globalization
USE_TZ                      = True
USE_I18N                    = True
USE_L10N                    = True
TIME_ZONE                   = 'UTC'
LANGUAGE_CODE               = 'en-us'
LANGUAGES                   = [('en', 'English'), ('pl', 'Polish')]


# Static and media
STATIC_URL                  = '/static/'
STATIC_ROOT                 = path.join(BASE_DIR, 'dist', 'static')
STATICFILES_DIRS            = []  # TODO: what does this do?
STATICFILES_STORAGE         = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL                   = '/media/'
MEDIA_ROOT                  = path.join(BASE_DIR, 'media')

FILE_UPLOAD_TEMP_DIR        = path.join(BASE_DIR, 'tmp')
FILE_UPLOAD_PERMISSIONS     = 0o644  # rw-r--r--
FILE_UPLOAD_MIN_MEMORY_SIZE = 1024   # 1.KB
FILE_UPLOAD_MAX_MEMORY_SIZE = (1024 * 1024) * 10  # 10.MB
DATA_UPLOAD_MAX_MEMORY_SIZE = FILE_UPLOAD_MAX_MEMORY_SIZE + (1024 * 1024)

ALLOWED_IMAGE_CONTENT_TYPES = ('image/gif', 'image/png', 'image/webp', 'image/jpeg')
ALLOWED_AUDIO_CONTENT_TYPES = ('audio/x-wav', 'audio/ogg', 'audio/webm', 'audio/mpeg')
ALLOWED_VIDEO_CONTENT_TYPES = ('video/x-msvideo', 'video/ogg', 'video/webm', 'video/mpeg')
ALLOWED_CONTENT_TYPES       = (
    *ALLOWED_IMAGE_CONTENT_TYPES, *ALLOWED_AUDIO_CONTENT_TYPES, *ALLOWED_VIDEO_CONTENT_TYPES
)



# Email
DEFAULT_FROM_EMAIL          = f'admin@{FQDN}'
SERVER_EMAIL                = f'server@{FQDN}'
EMAIL_SUBJECT_PREFIX        = f'{NAME} - '
EMAIL_HOST                  = c('email.host')
EMAIL_PORT                  = c('email.port')
EMAIL_HOST_USER             = c('email.user')
EMAIL_HOST_PASSWORD         = c('email.pass')
EMAIL_TIMEOUT               = c('email.timeout', cast=int)
EMAIL_BACKEND               = c('email.backend')
EMAIL_FILE_PATH             = FILE_UPLOAD_TEMP_DIR
EMAIL_USE_TLS               = c('email.use-tls', cast=bool)
EMAIL_USE_SSL               = c('email.use-ssl', cast=bool)
EMAIL_SSL_KEYFILE           = c('email.ssl-key')
EMAIL_SSL_CERTFILE          = c('email.ssl-cert')

if EMAIL_FILE_PATH[0] != '/':
    EMAIL_FILE_PATH = path.join(BASE_DIR, EMAIL_FILE_PATH)


# Decorators
PRETTIFY_CALLABLE           = 'prettify'
OWNERSHIP_REQUIRED_CALLABLE = 'get_owner'
OWNERSHIP_REQUIRED_PASS_OBJ = True


# Accounts
LOGIN_URL                   = 'account_login'
LOGIN_REDIRECT_URL          = ''
LOGOUT_REDIRECT_URL         = ''

ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGOUT_ON_GET           = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

AUTH_USER_MODEL                 = 'auth.User'
ACCOUNT_ADAPTER                 = 'allauth.account.adapter.DefaultAccountAdapter'
SOCIALACCOUNT_ADAPTER           = 'allauth.socialaccount.adapter.DefaultSocialAccountAdapter'

ACCOUNT_DEFAULT_HTTP_PROTOCOL   = SCHEME
ACCOUNT_AUTHENTICATION_METHOD   = 'username_email'
ACCOUNT_USERNAME_MIN_LENGTH     = 4
ACCOUNT_USERNAME_VALIDATORS     = ''
ACCOUNT_USERNAME_BLACKLIST      = []

ACCOUNT_EMAIL_REQUIRED          = True
ACCOUNT_UNIQUE_EMAIL            = True
ACCOUNT_EMAIL_VERIFICATION      = 'mandatory'
ACCOUNT_EMAIL_SUBJECT_PREFIX    = EMAIL_SUBJECT_PREFIX

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
    },
    'facebook': {
        'SCOPE': ['public_profile', 'email'],
        'FIELDS': ['email', 'name', 'verified', 'gender'],
    },
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


INSTALLED_APPS = [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.humanize',

    # plugins
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # app
    'backend.api',
    'manage',
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
    'django.middleware.cache.FetchFromCacheMiddleware',
]


MIDDLEWARE_CLASSES = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],

            'builtins': [
                'wypok.templatetags.markup',
                'wypok.templatetags.prettify',
                'wypok.templatetags.shortnaturaltime',
                'wypok.templatetags.get_default',
            ],
        },
    },
]


DATABASES = {
    'default': {
        'HOST':     c('db.host'),
        'PORT':     c('db.port'),
        'USER':     c('db.user'),
        'PASSWORD': c('db.pass'),
        'NAME':     c('db.name'),
        'ENGINE':   c('db.backend'),
    },
}

# Cache
CACHE_HOST                  = c('cache.host')
CACHE_PORT                  = c('cache.port')
CACHE_TTL                   = c('cache.ttl', cast=int)
CACHE_TIMEOUT               = c('cache.timeout', cast=int)
CACHE_BACKEND               = c('cache.backend')
CACHE_LOCATION              = f'{CACHE_HOST}:{CACHE_PORT}'

CACHES = {
    'default': {
        'LOCATION': c('cache.host') + ':' + c('cache.port', cast=str),
        'TIMEOUT':  c('cache.timeout', cast=int),
        'BACKEND':  c('cache.backend'),
    },
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': LOG_LEVEL,
            'class': 'logging.FileHandler',
            'filename': path.join(BASE_DIR, 'app.log'),
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
    },
}
