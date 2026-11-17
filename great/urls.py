from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/<str:name>/', views.view_result, name='view_result'),
]