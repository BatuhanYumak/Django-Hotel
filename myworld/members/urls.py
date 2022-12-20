from django.urls import path
from . import views
# Hier maak path's aan. Dit gebruik ik voor om de gebruiker naar een andere pagina te sturen.
urlpatterns = [
    path('', views.index, name='index'),
    path('hotels/', views.hotel, name='hotel'),
    path('amsterdam/', views.amsterdam, name='ams'),
    path('antwerpen/', views.antwerpen, name='antw'),
    path('athene/', views.athene, name='ath'),
    path('bangkok/', views.bangkok, name='bak'),
    path('barcelona/', views.barcelona, name='bar'),
    path('berlijn/', views.berlijn, name='ber'),

]



