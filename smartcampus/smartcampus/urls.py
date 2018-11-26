"""
smartcampus URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('home/', include('core.urls')),
    path('select_location/', include('core.urls')),
    path('campus_report/', include('core.urls')),
    path('feedback/', include('core.urls'))
]
