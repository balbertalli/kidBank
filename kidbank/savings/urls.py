"""URLs for savings app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/select/', views.select_account, name='select_account'),
    path('accounts/details/<uuid:uuid>', views.account_details, name='account_details'),
]