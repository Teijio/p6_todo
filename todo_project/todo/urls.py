from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "todo"

urlpatterns = [
    path("", include("posts.urls", namespace="posts")),
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
]

