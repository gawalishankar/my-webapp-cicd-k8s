from django.core.cache import cache
cache.set('key', 'value', timeout=60)

CACHES = {
  'default': {
    'BACKEND': 'django_redis.cache.RedisCache',
    'LOCATION': 'redis://redis:6379/1',
    'OPTIONS': {
        'CLIENT_CLASS': 'django_redis.client.DefaultClient',
    }
  }
}
