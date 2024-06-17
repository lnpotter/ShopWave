from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("signup/", views.signup, name="signup"),
    path("terms/", views.terms, name="terms"),
    path("policy/", views.policy, name="policy"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("login/", auth_views.LoginView.as_view(authentication_form=LoginForm), name="login")
]
