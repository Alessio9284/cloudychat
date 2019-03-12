from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('log/', views.logging, name = 'log'),
    path('reg/', views.registration, name = 'reg'),
    path('add/', views.adduser, name = 'add'),
    path('list/', views.userlist, name = 'list'),
    path('list/<nickname>/', views.chat, name = 'nickname'),

    #path('<int:domanda_id>/', views.dettagli, name = 'detail'),
]