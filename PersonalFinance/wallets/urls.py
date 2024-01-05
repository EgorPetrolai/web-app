from django.urls import path
from . import views

urlpatterns = [
    path('', views.wallets_home, name='wallets_home'),
    path('add_new_wallet', views.add_new_wallet, name='add_new_wallet'),
    path('<int:pk>', views.WalletDetailView.as_view(), name='wallets-detail')
]
