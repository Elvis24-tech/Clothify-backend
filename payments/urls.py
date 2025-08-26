from django.urls import path
from .views import lipa_na_mpesa, mpesa_callback

urlpatterns = [
    path('stkpush/', lipa_na_mpesa, name='stkpush'),
    path('callback/', mpesa_callback, name='mpesa_callback'),
]
