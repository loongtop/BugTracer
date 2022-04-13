# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': '127.0.0.1:6379',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#             'CONNECTION_POOL_KWARGS': {
#                 'max_connections': 1000,
#                 'encoding': 'utf-8'
#             },
#             'PASSWORD': 'yadayada',
#         },
#     },
#     'default2': {
#         # 用于读写分离（两台不同机器间有同步机制）
#     }
# }
