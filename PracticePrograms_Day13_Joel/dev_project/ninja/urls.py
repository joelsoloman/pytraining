from django.urls import path

from . import views

app_name = 'ninja'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:dev_id>/', views.details, name='details'),
    path('<int:dev_id>/level/', views.level, name='level')
]