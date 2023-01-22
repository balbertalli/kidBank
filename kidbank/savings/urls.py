"""URLs for savings app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]