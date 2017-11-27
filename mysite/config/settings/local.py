import random
import string

from .base import *

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.ap-northeast-2.compute.amazonaws.com',
    '.ap-northeast-2.elasticbeanstalk.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = ''.join([random.choice(string.ascii_lowercase) for i in range(40)])
