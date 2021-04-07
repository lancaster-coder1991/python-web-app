"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import (
    views as auth_views,
)  # this imports views from Django's authentication library
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("register/", user_views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),  # These are class-based views imported from Django's contrib library - ready made views for us to use for login/logout
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path("profile/", user_views.profile, name="profile"),
]

if (
    settings.DEBUG
):  # This code is requied in order to load images correctly. Because serving images with this method is only suitable for development (DEBUG mode in Django), we can use conditional logic to only include these path settings when in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)