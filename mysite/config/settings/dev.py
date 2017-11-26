from .base import *

config_secret = json.loads(open(CONFIG_SECRET_DEV_FILE).read())

# AWS
AWS_ACCESS_KEY_ID = config_secret_common['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret_common['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret_common['aws']['s3_bucket_name']

# AWS Storage
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'
# S3 FileStorage
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'


DATABASES = config_secret['django']['databases']