from django.urls import path, include
from users.api.api import UserApiView

urlpatterns = [
    path('usuario/', UserApiView.as_view(), name='usuarioapi')
]