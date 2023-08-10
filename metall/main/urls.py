
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form', views.form, name='form'),
    path('contacts', views.contacts, name='contacts'),
    path('form/success', views.success, name='success'),
    path('prices', views.prices, name='prices'),
    path('cards', views.cards, name='cards')
]