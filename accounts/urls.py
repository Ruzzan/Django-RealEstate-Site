from django.urls import path
from .import views
urlpatterns = [
    path('signup/',views.SignupView, name='signup'),
    path('login/',views.LoginView, name='login'),
    path('logout/',views.LogoutView,name='logout'),
    path('dashboard/',views.DashboardView,name='dashboard'),
]