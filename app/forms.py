from django import forms

from .models import Account, Ip, Offer


class IpForm(forms.ModelForm):
    class Meta:
        model = Ip
        fields = ['ip']


class AccountForm(forms.ModelForm):
    ip = forms.GenericIPAddressField(label='IP адрес')
    class Meta:
        model = Account
        fields = ['offer', 'post', 'password', 'config_number', 'creator']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['offer'].widget.attrs.update({'class': 'form-control'})  
        self.fields['creator'].widget.attrs.update({'class': 'form-control'})

    def clean_ip(self):
        ip_address = self.cleaned_data['ip']
        offer = self.cleaned_data['offer']
        try:
            Ip.objects.get(ip=ip_address, country__offer__title=offer)
            raise forms.ValidationError("IP-адрес уже использовался.")
        except Ip.DoesNotExist:
            pass
        return ip_address

    def save(self, commit=True):
        account = super().save()
        ip_address = self.cleaned_data.get('ip')
        Ip.objects.create(ip=ip_address, country=account.offer.country, account=account)

        return account