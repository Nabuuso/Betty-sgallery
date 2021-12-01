from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('search/', views.search_images, name='search_results'),
    path('results/', views.get_image, name='image_results'),
    path('location/', views.location, name='location_results'),
    path('category/', views.category, name='category_results'),
]
