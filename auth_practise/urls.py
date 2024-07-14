from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.user_logout, name="logout"),
    path("change_pass/", views.change_password, name="change_pass"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("forget_password/", views.forget_password, name="forget_password"),
]
