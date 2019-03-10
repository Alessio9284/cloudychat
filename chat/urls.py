from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('reg/', views.registration, name = 'reg'),
    path('list/', views.userlist, name = 'list'),
    path('list/<nickname>/', views.chat, name = 'nickname'),

    #path('<int:domanda_id>/', views.dettagli, name = 'detail'),
]