from django.contrib import admin
from django.urls import path
from .views import LogInView, LogOutView, SignUpView

urlpatterns = [
    path('login/', LogInView.as_view()),
    path('logout/', LogOutView.as_view()),
    path('signup/', SignUpView.as_view()),
]