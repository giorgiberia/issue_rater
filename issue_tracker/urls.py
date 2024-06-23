"""
URL configuration for issue_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include   # Include 'include' for the URLs

from issues.views import register, user_login, user_logout, issue_list_and_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('issues/', include('issues.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's auth URLs
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', issue_list_and_create, name='issue_list_and_create')

]


