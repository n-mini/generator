from django.urls import path
from . import views

app_name= 'generator'
urlpatterns = [
    # viewsからindexを読み込んで、nameをindexに
    path('', views.index, name='index'),
    path('GET',views.get, name='get')

]
