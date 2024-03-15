from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('greeting/<str:name>/', views.greeting),
    path('<int:num>/', views.detail),
]
