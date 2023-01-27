from django.contrib import admin
from django.urls import include, path
from django.urls import path
from django.urls import path
# from members.views import logout_view

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),  
    # path('logout/', logout_view, name='logout'),


]


