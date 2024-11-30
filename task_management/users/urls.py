from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),  # Root path
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
