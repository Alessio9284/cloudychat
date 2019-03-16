from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('log/', views.logging, name = 'log'),
    path('reg/', views.registration, name = 'reg'),
    path('add/', views.adduser, name = 'add'),
    path('list/', views.userlist, name = 'list'),
    path('list/<nickname>/', views.chat, name = 'nickname'),
    path('update/list/', views.updatelist, name = 'up_list'),
    path('update/messages/', views.updatemessages, name = 'up_messages'),

    #https://stackoverflow.com/questions/13465711/how-do-i-post-with-jquery-ajax-in-django

    #path('<int:domanda_id>/', views.dettagli, name = 'detail'),
]