from django.urls import path

from . import views

app_name = "webapp"
urlpatterns = [
path("signup/", views.signup, name ="signup"),
path("signin/", views.signin, name = "signin"),
path("home/", views.homeview, name="home"),
]