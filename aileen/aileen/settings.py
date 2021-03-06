import logging.config
import os
import sys

TRUTH_STRINGS = ["True", "true", "1", "t", "y", "yes"]


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY", default="wpqb4)9vq85zf$!f=x6@t75v0j*-nb^dizdjy(hovma57g*bgv"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", default="yes") in TRUTH_STRINGS

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "bootstrap3",
    "leaflet",
    "djgeojson",
    "data",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "aileen.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "aileen.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Amsterdam"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "assets")

LOGIN_REDIRECT_URL = "server:home"
LOGOUT_REDIRECT_URL = "server:logout"

# LEAFLET_CONFIG is needed to configure leaflet
LEAFLET_CONFIG = {
    "DEFAULT_CENTER": (52.2, 4.7),
    "DEFAULT_ZOOM": 10,
    "RESET_VIEW": False,
}


# --- Custom logging config

LOGGING_CONFIG = None

aileen_logging_config = {
    "version": 1,
    "formatters": {
        "default": {"format": "[Aileen][%(asctime)s] %(levelname)s: %(message)s"},
        "detail": {
            "format": "[Aileen][%(asctime)s] %(levelname)s: %(message)s [log made in %(pathname)s:%(lineno)d]"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "default",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "detail",
            "filename": BASE_DIR + "/aileen.log",
        },
    },
    "root": {"level": "INFO", "handlers": ["console", "file"], "propagate": True},
}

logging.config.dictConfig(aileen_logging_config)


# -------- Custom settings added by the Aileen team ----------
#  ----- some can be customised by environment variables ----

AILEEN_MODE = os.environ.get(
    "AILEEN_MODE", default="box"
)  # can also be "server" or "both" (for dev purposes)
if AILEEN_MODE in ("box", "both"):
    INSTALLED_APPS.extend(("box", "calibration"))
if AILEEN_MODE in ("server", "both"):
    INSTALLED_APPS.append("server")

#  ---- General Settings

# Display this in front of simply stdout printing
TERM_LBL = "[Aileen]"

#  ---- Box Settings
BOX_PORT = os.environ.get("BOX_PORT", default = 80)
# The wifi interface names on which your device might sit.
# Factory identifier and maybe the one airmon uses after it ran. Use a comma-separated list for more than one.
WIFI_INTERFACES = os.environ.get("WIFI_INTERFACES", default="wlan1")
FULL_PATH_TO_AIRMON_NG = os.environ.get("FULL_PATH_TO_AIRMON_NG", default="airmon-ng")
FULL_PATH_TO_AIRODUMP = os.environ.get("FULL_PATH_TO_AIRODUMP", default="airodump-ng")
# This interval is how frequently we log monitored devices to file
AIRODUMP_LOG_INTERVAL_IN_SECONDS = int(
    os.environ.get("AIRODUMP_LOG_INTERVAL_IN_SECONDS", default=5)
)
# You can store the sudo password here if you need to automate starting the airocrack tools.
SUDO_PWD = os.environ.get("SUDO_PWD", default="")
# If you have installed aileen in a virtual env, the tmux session needs to know how to get that activated.
ACTIVATE_VENV_CMD = os.environ.get("ACTIVATE_VENV_CMD", default="")
ACTIVATE_VENV_CMD = (
    f"{ACTIVATE_VENV_CMD};"
    if ACTIVATE_VENV_CMD and not ACTIVATE_VENV_CMD.endswith(";")
    else ACTIVATE_VENV_CMD
)

UPLOAD_INTERVAL_IN_SECONDS = int(
    os.environ.get("UPLOAD_INTERVAL_IN_SECONDS", default=60)
)
UPLOAD_MAX_NUMBER_PER_REQUEST = int(
    os.environ.get("UPLOAD_MAX_NUMBER_PER_REQUEST", default=500)
)
STATUS_MONITORING_INTERVAL_IN_SECONDS = int(
    os.environ.get("STATUS_MONITORING_INTERVAL_IN_SECONDS", default=60)
)
PROCESS_RESTART_INTERVAL_IN_SECONDS = int(
    os.environ.get("PROCESS_RESTART_INTERVAL_IN_SECONDS", default=600)
)

if PROCESS_RESTART_INTERVAL_IN_SECONDS % STATUS_MONITORING_INTERVAL_IN_SECONDS != 0:
    print(
        "Configuration problem in aileen/settings.py: Please make PROCESS_RESTART_INTERVAL_IN_SECONDS (now %d)"
        " a multiple of STATUS_MONITORING_INTERVAL_IN_SECONDS (%d)."
        % (PROCESS_RESTART_INTERVAL_IN_SECONDS, STATUS_MONITORING_INTERVAL_IN_SECONDS)
    )
    sys.exit(2)

# whether to hash mac addresses, defaults true
HASH_MAC_ADDRESSES = (
    os.environ.get("HASH_MAC_ADDRESSES", default="True") in TRUTH_STRINGS
)
HASH_ITERATIONS = int(
    os.environ.get("HASH_ITERATIONS", default=500_000)
)  # 2013 they recommended "at least 100000"

# whether boxes should upload events to the server
UPLOAD_EVENTS = os.environ.get("UPLOAD_EVENTS", default="False") in TRUTH_STRINGS

# For tmux sessions and writing info to DB
TMUX_SESSION_NAME = "aileen_tmux_session"
# Name of temporary folder for airodump output
TMP_DIR_NAME = "aileen_device_detection_data"
# Use this as file prefix when airodump runs
AIRODUMP_FILE_PREFIX = "full_airodump_file"


#  ---- Server Settings
