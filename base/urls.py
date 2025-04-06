from django.urls import path
from .views import register, login_view, homepage, pomodoro_timer
from .views import journal_list, journal_create, journal_edit

urlpatterns = [
    path('', homepage, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('timer/', pomodoro_timer, name='timer'),

    path('journal/', journal_list, name='journal_list'),
    path('journal/new/', journal_create, name='journal_create'),
    path('journal/<int:pk>/edit/', journal_edit, name='journal_edit'),
]
