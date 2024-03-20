from django.shortcuts import render, redirect
from .forms import AccountForm
from .models import Partner, Offer, Account

from django.http import JsonResponse
from django.utils import timezone
import random
import string

def index_view(request):
    partners = Partner.objects.all()
    return render(request, 'index.html', context={'partners': partners})


def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('index')
    else:
        form = AccountForm()
    return render(request, 'create_account.html', {'form': form})

def generate_random_credentials(request):
    print(Offer.objects.get(pk=request.GET.get('offer')).country)
    login = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
    return JsonResponse({'login': login, 'password': password})

def check_account_age(request):
    config_number = request.GET.get('config_number')

    account = Account.objects.filter(config_number=config_number).order_by('-date').first()
    if account:
        today = timezone.now()
        account_age = (today - account.date).days
    else:
        account_age = 'Не использовался'
    return JsonResponse({'account_age': account_age})