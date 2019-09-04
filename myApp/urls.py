from django.urls import path
from .import views
urlpatterns = [
    path('', views.Test,name='home'),
    path('about/', views.About, name='about'),
    path('detail/<int:id>/', views.Detail, name='detail'),
    path('listing/', views.Listing, name='listing'),
    path('search/',views.SearchView, name='search'),
]
