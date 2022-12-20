from django.contrib import admin
from django.urls import include, path
from django.urls import path
from . import views

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),    
]


urlpatterns = [
    path('login/', views.login_view, name='login'),
]

