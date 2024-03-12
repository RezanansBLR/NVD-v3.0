from django.urls import path
from .views import index_view, create_account

urlpatterns = [
    path('', index_view, name='index'),
    path('create_account/', create_account, name='create_account'),
]