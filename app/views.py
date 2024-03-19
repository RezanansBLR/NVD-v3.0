from django.shortcuts import render, redirect
from .forms import AccountForm
from datetime import datetime

from .models import Partner


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