from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='main'),
	path('result/', views.result, name='result'),
    path('history/', views.history, name='history'),
]