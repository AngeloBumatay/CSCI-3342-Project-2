from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('movie/<int:movie_id>/', views.movie_single, name='movie_single')
]