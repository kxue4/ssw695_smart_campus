"""smartcampus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('select_location/', views.select_location, name='select location'),
    path('campus_report/', views.campus_report, name='campus report'),
    path('feedback/', views.feedback, name='feedback'),
    path('campus_report/report_2018_07_28', views.report_2018_07_28, name='report_2018_07_28'),
    # path('post-feedback/', views.post_feedback, name='post-feedback'),
    
]
