from django.shortcuts import render, redirect
from .forms import AccountForm
from .models import Partner, Offer, Account, Ip

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

def check_config(request):
    config_number = request.GET.get('config_number')

    account = Account.objects.filter(config_number=config_number).order_by('-date').first()
    if account:
        today = timezone.now()
        config_info = (today - account.date).days
    else:
        config_info = 'Не использовался'
    return JsonResponse({'config_info': config_info})

def check_ip(request):
    ip = request.GET.get('ip')
    offer = request.GET.get('offer')

    try:
        Ip.objects.get(ip=ip, country__offer__pk=offer)
        ip_info = 'IP-адрес уже использовался!'
    except Ip.DoesNotExist:
        ip_info = 'IP-адрес уникальный'
    
    return JsonResponse({'ip_info': ip_info})
