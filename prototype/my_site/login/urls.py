from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("authenticate", views.authenticate, name="authenticate"),
    path("callback", views.callback, name="auth_callback"),
]
