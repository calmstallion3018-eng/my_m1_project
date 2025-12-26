from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('yarlens/', views.yarlens, name='yarlens'),
    path('mezon/', views.mezon, name='mezon'),
    path('kanamestone/', views.kanamestone, name='kanamestone'),
    path('evers1/', views.evers1, name='evers1'),
    path('shinkujessica/', views.shinkujessica, name='shinkujessica'),
    path('yoneda2000/', views.yoneda2000, name='yoneda2000'),
    path('takuro1/', views.takuro1, name='takuro1'),
    path('dondecollete1/', views.dondecollete1, name='dondecollete1'),
    path('gokaicaptain/', views.gokaicaptain, name='gokaicaptain'),
    path('mamatarte/', views.mamatarte, name='mamatarte'),
    path('dondecollete2/', views.dondecollete2, name='dondecollete2'),
    path('evers2/', views.evers2, name='evers2'),
    path('takuro2/', views.takuro2, name='takuro2'),
]