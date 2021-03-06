#coding:utf-8

 ABSOLUTE_URL_OVERRIDES = {dict} {}
 ADMINS = {list} []
 ALLOWED_HOSTS = {list} []
 APPEND_SLASH = {bool} True
 AUTHENTICATION_BACKENDS = {list} [u'django.contrib.auth.backends.ModelBackend']
 AUTH_PASSWORD_VALIDATORS = {list} [{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'}, {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'}, {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'}, {'NAME': 'django
 AUTH_USER_MODEL = {unicode} u'auth.User'
 BASE_DIR = {str} 'G:\\github\\django-learning\\django-learning\\project'
 CACHES = {dict} {'default': {'OPTIONS': {}, 'LOCATION': ['redis://192.168.10.100:6379'], 'BACKEND': 'django_redis.cache.RedisCache'}}
 CACHE_MIDDLEWARE_ALIAS = {unicode} u'default'
 CACHE_MIDDLEWARE_KEY_PREFIX = {unicode} u''
 CACHE_MIDDLEWARE_SECONDS = {int} 600
 CSRF_COOKIE_AGE = {int} 31449600
 CSRF_COOKIE_DOMAIN = {NoneType} None
 CSRF_COOKIE_HTTPONLY = {bool} False
 CSRF_COOKIE_NAME = {unicode} u'csrftoken'
 CSRF_COOKIE_PATH = {unicode} u'/'
 CSRF_COOKIE_SECURE = {bool} False
 CSRF_FAILURE_VIEW = {unicode} u'django.views.csrf.csrf_failure'
 CSRF_HEADER_NAME = {unicode} u'HTTP_X_CSRFTOKEN'
 CSRF_TRUSTED_ORIGINS = {list} []
 DATABASES = {dict} {'default': {'ENGINE': 'django.db.backends.sqlite3', 'AUTOCOMMIT': True, 'ATOMIC_REQUESTS': False, 'NAME': 'G:\\github\\django-learning\\django-learning\\project\\db.sqlite3', 'CONN_MAX_AGE': 0, 'TIME_ZONE': None, 'PORT': '', 'HOST': '', 'USER': '', 'TEST'
 DATABASE_ROUTERS = {list} []
 DATA_UPLOAD_MAX_MEMORY_SIZE = {int} 2621440
 DATA_UPLOAD_MAX_NUMBER_FIELDS = {int} 1000
 DATETIME_FORMAT = {unicode} u'N j, Y, P'
 DATETIME_INPUT_FORMATS = {list} [u'%Y-%m-%d %H:%M:%S', u'%Y-%m-%d %H:%M:%S.%f', u'%Y-%m-%d %H:%M', u'%Y-%m-%d', u'%m/%d/%Y %H:%M:%S', u'%m/%d/%Y %H:%M:%S.%f', u'%m/%d/%Y %H:%M', u'%m/%d/%Y', u'%m/%d/%y %H:%M:%S', u'%m/%d/%y %H:%M:%S.%f', u'%m/%d/%y %H:%M', u'%m/%d/%y']
 DATE_FORMAT = {unicode} u'N j, Y'
 DATE_INPUT_FORMATS = {list} [u'%Y-%m-%d', u'%m/%d/%Y', u'%m/%d/%y', u'%b %d %Y', u'%b %d, %Y', u'%d %b %Y', u'%d %b, %Y', u'%B %d %Y', u'%B %d, %Y', u'%d %B %Y', u'%d %B, %Y']
 DEBUG = {bool} True
 DEBUG_PROPAGATE_EXCEPTIONS = {bool} False
 DECIMAL_SEPARATOR = {unicode} u'.'
 DEFAULT_CHARSET = {unicode} u'utf-8'
 DEFAULT_CONTENT_TYPE = {unicode} u'text/html'
 DEFAULT_EXCEPTION_REPORTER_FILTER = {unicode} u'django.views.debug.SafeExceptionReporterFilter'
 DEFAULT_FILE_STORAGE = {unicode} u'django.core.files.storage.FileSystemStorage'
 DEFAULT_FROM_EMAIL = {unicode} u'webmaster@localhost'
 DEFAULT_INDEX_TABLESPACE = {unicode} u''
 DEFAULT_TABLESPACE = {unicode} u''
 DISALLOWED_USER_AGENTS = {list} []
 EMAIL_BACKEND = {unicode} u'django.core.mail.backends.smtp.EmailBackend'
 EMAIL_HOST = {unicode} u'localhost'
 EMAIL_HOST_PASSWORD = {unicode} u''
 EMAIL_HOST_USER = {unicode} u''
 EMAIL_PORT = {int} 25
 EMAIL_SSL_CERTFILE = {NoneType} None
 EMAIL_SSL_KEYFILE = {NoneType} None
 EMAIL_SUBJECT_PREFIX = {unicode} u'[Django] '
 EMAIL_TIMEOUT = {NoneType} None
 EMAIL_USE_SSL = {bool} False
 EMAIL_USE_TLS = {bool} False
 FILE_CHARSET = {unicode} u'utf-8'
 FILE_UPLOAD_DIRECTORY_PERMISSIONS = {NoneType} None
 FILE_UPLOAD_HANDLERS = {list} [u'django.core.files.uploadhandler.MemoryFileUploadHandler', u'django.core.files.uploadhandler.TemporaryFileUploadHandler']
 FILE_UPLOAD_MAX_MEMORY_SIZE = {int} 2621440
 FILE_UPLOAD_PERMISSIONS = {NoneType} None
 FILE_UPLOAD_TEMP_DIR = {NoneType} None
 FIRST_DAY_OF_WEEK = {int} 0
 FIXTURE_DIRS = {list} []
 FORCE_SCRIPT_NAME = {NoneType} None
 FORMAT_MODULE_PATH = {NoneType} None
 IGNORABLE_404_URLS = {list} []
 INSTALLED_APPS = {list} ['django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles']
 INTERNAL_IPS = {list} []
 LANGUAGES = {list} [(u'af', u'Afrikaans'), (u'ar', u'Arabic'), (u'ast', u'Asturian'), (u'az', u'Azerbaijani'), (u'bg', u'Bulgarian'), (u'be', u'Belarusian'), (u'bn', u'Bengali'), (u'br', u'Breton'), (u'bs', u'Bosnian'), (u'ca', u'Catalan'), (u'cs', u'Czech'), (u'cy', u'Welsh
 LANGUAGES_BIDI = {list} [u'he', u'ar', u'fa', u'ur']
 LANGUAGE_CODE = {str} 'en-us'
 LANGUAGE_COOKIE_AGE = {NoneType} None
 LANGUAGE_COOKIE_DOMAIN = {NoneType} None
 LANGUAGE_COOKIE_NAME = {unicode} u'django_language'
 LANGUAGE_COOKIE_PATH = {unicode} u'/'
 LOCALE_PATHS = {list} []
 LOGGING = {dict} {}
 LOGGING_CONFIG = {unicode} u'logging.config.dictConfig'
 LOGIN_REDIRECT_URL = {unicode} u'/accounts/profile/'
 LOGIN_URL = {unicode} u'/accounts/login/'
 LOGOUT_REDIRECT_URL = {NoneType} None
 MANAGERS = {list} []
 MEDIA_ROOT = {unicode} u''
 MEDIA_URL = {unicode} u''
 MESSAGE_STORAGE = {unicode} u'django.contrib.messages.storage.fallback.FallbackStorage'
 MIDDLEWARE = {list} ['django.middleware.security.SecurityMiddleware', 'django.contrib.sessions.middleware.SessionMiddleware', 'django.middleware.common.CommonMiddleware', 'django.middleware.csrf.CsrfViewMiddleware', 'django.contrib.auth.middleware.AuthenticationMiddleware', '
 MIDDLEWARE_CLASSES = {list} [u'django.middleware.common.CommonMiddleware', u'django.middleware.csrf.CsrfViewMiddleware']
 MIGRATION_MODULES = {dict} {}
 MONTH_DAY_FORMAT = {unicode} u'F j'
 NUMBER_GROUPING = {int} 0
 PASSWORD_HASHERS = {list} [u'django.contrib.auth.hashers.PBKDF2PasswordHasher', u'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher', u'django.contrib.auth.hashers.Argon2PasswordHasher', u'django.contrib.auth.hashers.BCryptSHA256PasswordHasher', u'django.contrib.auth.hashers.BCr
 PASSWORD_RESET_TIMEOUT_DAYS = {int} 3
 PREPEND_WWW = {bool} False
 ROOT_URLCONF = {str} 'project.urls'
 SECRET_KEY = {str} '9f)%86ix-+01ldd&%&=&x$g@7u1i4cy76)gt(2d5d(s#amrk&j'
 SECURE_BROWSER_XSS_FILTER = {bool} False
 SECURE_CONTENT_TYPE_NOSNIFF = {bool} False
 SECURE_HSTS_INCLUDE_SUBDOMAINS = {bool} False
 SECURE_HSTS_SECONDS = {int} 0
 SECURE_PROXY_SSL_HEADER = {NoneType} None
 SECURE_REDIRECT_EXEMPT = {list} []
 SECURE_SSL_HOST = {NoneType} None
 SECURE_SSL_REDIRECT = {bool} False
 SERVER_EMAIL = {unicode} u'root@localhost'
 SESSION_CACHE_ALIAS = {unicode} u'default'
 SESSION_COOKIE_AGE = {int} 1209600
 SESSION_COOKIE_DOMAIN = {NoneType} None
 SESSION_COOKIE_HTTPONLY = {bool} True
 SESSION_COOKIE_NAME = {unicode} u'sessionid'
 SESSION_COOKIE_PATH = {unicode} u'/'
 SESSION_COOKIE_SECURE = {bool} False
 SESSION_ENGINE = {unicode} u'django.contrib.sessions.backends.db'
 SESSION_EXPIRE_AT_BROWSER_CLOSE = {bool} False
 SESSION_FILE_PATH = {NoneType} None
 SESSION_SAVE_EVERY_REQUEST = {bool} False
 SESSION_SERIALIZER = {unicode} u'django.contrib.sessions.serializers.JSONSerializer'
 SETTINGS_MODULE = {str} 'project.settings'
 SHORT_DATETIME_FORMAT = {unicode} u'm/d/Y P'
 SHORT_DATE_FORMAT = {unicode} u'm/d/Y'
 SIGNING_BACKEND = {unicode} u'django.core.signing.TimestampSigner'
 SILENCED_SYSTEM_CHECKS = {list} []
 STATICFILES_DIRS = {list} []
 STATICFILES_FINDERS = {list} [u'django.contrib.staticfiles.finders.FileSystemFinder', u'django.contrib.staticfiles.finders.AppDirectoriesFinder']
 STATICFILES_STORAGE = {unicode} u'django.contrib.staticfiles.storage.StaticFilesStorage'
 STATIC_ROOT = {NoneType} None
 STATIC_URL = {str} '/static/'
 TEMPLATES = {list} [{'DIRS': ['G:\\github\\django-learning\\django-learning\\project\\templates'], 'APP_DIRS': True, 'OPTIONS': {'context_processors': ['django.template.context_processors.debug', 'django.template.context_processors.request', 'django.contrib.auth.context_proc
 TEST_NON_SERIALIZED_APPS = {list} []
 TEST_RUNNER = {unicode} u'django.test.runner.DiscoverRunner'
 THOUSAND_SEPARATOR = {unicode} u','
 TIME_FORMAT = {unicode} u'P'
 TIME_INPUT_FORMATS = {list} [u'%H:%M:%S', u'%H:%M:%S.%f', u'%H:%M']
 TIME_ZONE = {str} 'UTC'
 USE_ETAGS = {bool} False
 USE_I18N = {bool} True
 USE_L10N = {bool} True
 USE_THOUSAND_SEPARATOR = {bool} False
 USE_TZ = {bool} True
 USE_X_FORWARDED_HOST = {bool} False
 USE_X_FORWARDED_PORT = {bool} False
 WSGI_APPLICATION = {str} 'project.wsgi.application'
 X_FRAME_OPTIONS = {unicode} u'SAMEORIGIN'
 YEAR_MONTH_FORMAT = {unicode} u'F Y'
