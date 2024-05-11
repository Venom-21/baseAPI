from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiCheck),
    path('login/', include('baseFolder.login.loginRouter')),
]
