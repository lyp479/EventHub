from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:primary_key>/', views.event_detail, name='event_detail'),

]
