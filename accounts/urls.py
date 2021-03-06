"""IdeaBox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from accounts.views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('forget/', forget_view, name='forget'),
    path('forget_support/', forget_support_view, name='forget-support'),
    path('reset/<user>/<token>', reset_password, name='reset-password'),
    path('preferences/', preferences_view, name='preferences'),
    path('help/', help_view, name='help'),
    path('password_reset/', password_reset, name='password-reset'),
]
