from django.urls import path
from .views import register, login_view, homepage, pomodoro_timer

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('', homepage, name='home'),
    path('timer/', pomodoro_timer, name='timer'),
]
