from django.urls import path

#url Fo a Home PAge

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]
