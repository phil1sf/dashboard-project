from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('details/<int:panel_id>/', views.panel_details, name="panel_details"),
    
]
