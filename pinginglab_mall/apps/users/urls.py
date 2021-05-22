from django.urls import path
from .views import UsernameCountView

urlpatterns = [
    path('usernames/<username:username>/count/', UsernameCountView.as_view()),
]