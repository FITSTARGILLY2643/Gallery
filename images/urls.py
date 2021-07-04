from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns =[
    path('', views.index, name = 'index'),
    path('gallery/', views.gallery, name='gallery'),
    path('search/category', views.search_results, name='search_results'),
    path('search/location', views.search_location, name='search_location'),
  
]