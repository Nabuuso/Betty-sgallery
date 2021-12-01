from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path(r'^search/', views.search_images, name='search_results'),
    path(r'^image/(\d+)', views.get_image, name='image_results'),
    path(r'^location/(?P<location>\w{0,50})/', views.location, name='location_results'),
    path(r'^category/(?P<category>\w{0,50})/', views.category, name='category_results'),
]
