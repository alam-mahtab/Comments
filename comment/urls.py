"""comment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from comThread.views import CommentsAPI, AddCommentAPI, DeleteCommentAPI, EditCommentAPI
from rest_framework import routers, serializers, viewsets
from comThread.models import Comments
from rest_framework.response import Response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CommentsAPI.as_view()),
    path('get/', CommentsAPI.as_view()),
    path('add/', AddCommentAPI.as_view()),
    path('delete/', DeleteCommentAPI.as_view()),
    path('put/', EditCommentAPI.as_view())
]
