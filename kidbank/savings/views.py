from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from savings.models import Account

# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required
def select_account(request):
    permissions = request.user.get_all_permissions()
    if not 'savings.add_deposit' in permissions:
        accounts = Account.objects.filter(owner=request.user)
    else:
        accounts = Account.objects.all()
    return render(request, 'select_account.html', {'accounts': accounts})
    
    
    
@login_required
def account_details(request, uuid):
    account = Account.objects.get(uuid=uuid)
    return render(request, 'account_details.html', {'account': account})
    