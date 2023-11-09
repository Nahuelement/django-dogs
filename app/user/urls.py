"""
URL mappings for the user API.
"""
from django.urls import path

from user import views


app_name = 'auth'

urlpatterns = [
    path('', views.TokenView.as_view(), name='token'),
]
