from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('about', views.about, name='about'),
]
