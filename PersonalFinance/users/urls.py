from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
