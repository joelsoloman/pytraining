from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dev_id>/', views.details, name='details'),
]