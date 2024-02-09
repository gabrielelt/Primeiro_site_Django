from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', LoginView.as_view(), name='login'),
    path('home/', views.home, name='home'),
]