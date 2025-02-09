# blog\urls.py ГЛАВНЫЙ
from django.contrib import admin
from django.urls import path, include
from PythonBlog.views import main

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main),
    path("posts/", include("PythonBlog.urls")),
]
