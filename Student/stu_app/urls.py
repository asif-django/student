"""Student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from .views import add_student, view_student, details_student, delete_student

urlpatterns = [
    path('add/', add_student, name="add"),
    path('', view_student, name="view"),
    path('detail/<int:stu_id>', details_student, name="detail"),
    path('delete/<int:stu_id>', delete_student, name="delete"),
]
