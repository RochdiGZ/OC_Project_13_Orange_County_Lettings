from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.lettings, name='letting'),
]
