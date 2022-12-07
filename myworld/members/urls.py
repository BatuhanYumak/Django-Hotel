from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotels/', views.hotel, name='hotel'),
]

# urlpatterns(r'^$', 'index', name='index'),
# urlpatterns(r'^blog$', 'horel', name='blog'),