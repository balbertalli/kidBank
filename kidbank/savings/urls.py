"""URLs for savings app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/select/', views.select_account, name='select_account'),
    path('accounts/details/<uuid:uuid>', views.account_details, name='account_details'),
    path('accounts/deposit/<uuid:uuid>', views.deposit, name='deposit'),
    path('accounts/withdrawal/<uuid:uuid>', views.withdrawal, name='withdrawal'),
    path('accounts/transaction/edit/<int:transaction_id>', views.edit_transaction, name='edit_transaction'),
    path('accounts/transaction/delete/<int:transaction_id>',
         views.delete_transaction, name='delete_transaction'),
]