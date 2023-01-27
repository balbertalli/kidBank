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


@login_required
def edit_transaction(request, transaction_id):
    transaction = Transaction.objects.get(pk=transaction_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        form.save()
        return redirect('account_details', uuid=transaction.account.uuid)
    else:
        form = TransactionForm(instance=transaction)
        return render(request, 'edit_transaction.html', {'form': form, 'transaction': transaction })
    
    
@login_required
def delete_transaction(request, transaction_id):
    transaction = Transaction.objects.get(pk=transaction_id)
    transaction.delete()
    return redirect('account_details', uuid=transaction.account.uuid)