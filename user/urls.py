from django.urls import path

from .views import RegisterView
from . import views


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/',  views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
