from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('index_detail/<slug:slug>/', views.index_detail, name='index_detail'),
]