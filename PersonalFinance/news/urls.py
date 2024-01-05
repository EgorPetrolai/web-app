from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('add_new_news', views.add_new_news, name='add_new_news'),
    path('<int:pk>', views.WalletDetailView.as_view(), name='news-detail')
]
