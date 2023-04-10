
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from myapp import views

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/hello/', views.HelloAPI.as_view(), name='HelloAPI'),
    path('api/hello2/', views.hello_drf, name='hello_drf'),
    path('api/hellorole/', views.HelloRole.as_view(), name='HelloRole'),
    path('api/hellorole2/', views.HelloRole2.as_view(), name='HelloRole2'),
]
