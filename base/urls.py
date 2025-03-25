from django.urls import path
from .views import register, login_view, homepage

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('', homepage, name='home'),
]
