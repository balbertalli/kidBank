from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from savings.models import Account, Transaction, TransactionForm

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


@login_required
def deposit(request, uuid):
    account = Account.objects.get(uuid=uuid)
    if request.method == 'POST':
        dep = Transaction(account=account, type=1)
        form = TransactionForm(request.POST, instance=dep)
        form.save()
        return redirect('account_details', uuid=uuid)
    else:
        form = TransactionForm()
        return render(request, 'deposit.html', {'form': form, 'account': account})
    
    
@login_required
def withdrawal(request, uuid):
    account = Account.objects.get(uuid=uuid)
    if request.method == 'POST':
        wit = Transaction(account=account, type=0)
        form = TransactionForm(request.POST, instance=wit)
        form.save()
        return redirect('account_details', uuid=uuid)
    else:
        form = TransactionForm()
        return render(request, 'withdrawal.html', {'form': form, 'account': account})
    