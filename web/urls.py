from django.urls import re_path
from web.views import account


urlpatterns = [
    # re_path(r'^login/$', login.LoginView.as_view(), name='login'),
    re_path(r'register/$', account.RegisterView.as_view(), name='register'),
]