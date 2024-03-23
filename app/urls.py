from django.urls import path
from .views import index_view, create_account, generate_random_credentials, check_config, check_ip

urlpatterns = [
    path('', index_view, name='index'),
    path('create_account/', create_account, name='create_account'),

    path('generate-credentials/', generate_random_credentials, name='generate_credentials'),
    path('check_config/', check_config, name='check_config'),
    path('check_ip/', check_ip, name='check_ip'),
]