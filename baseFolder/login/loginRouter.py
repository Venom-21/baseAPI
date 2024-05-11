from django.urls import path
from .loginComponent import LoginAPI

urlpatterns = [
    path('GetLoginDetails', LoginAPI.as_view(), name='GetLoginDetails'),
    path('CreateUserAddress', LoginAPI.as_view(), name='CreateUserAddress'),
    path('loginOut', LoginAPI.as_view(), name='loginOut'),
]
