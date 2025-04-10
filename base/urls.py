from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    register, login_view, homepage, pomodoro_timer,
    journal_list, journal_create, journal_edit,
    stress_tips_list, toggle_tip_like, submit_tip_comment, saved_tips,
    affirmation_list, submit_affirmation_comment,
    toggle_affirmation_like, saved_affirmations, relaxation_list,
    relaxation_detail, journal_delete
)

urlpatterns = [
    path('', homepage, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('timer/', pomodoro_timer, name='timer'),

    # journal
    path('journal/', journal_list, name='journal_list'),
    path('journal/new/', journal_create, name='journal_create'),
    path('journal/<int:pk>/edit/', journal_edit, name='journal_edit'),
    path('journal/<int:pk>/delete/', journal_delete, name='journal_delete'),

    # stress tips
    path('tips/', stress_tips_list, name='stress_tips'),
    path('tips/<int:tip_id>/like/', toggle_tip_like, name='toggle_tip_like'),
    path('tips/<int:tip_id>/comment/', submit_tip_comment, name='submit_tip_comment'),
    path('tips/saved/', saved_tips, name='saved_tips'),

    # affirmations
    path('affirmations/', affirmation_list, name='affirmations'),
    path('affirmations/<int:affirmation_id>/comment/', submit_affirmation_comment, name='submit_affirmation_comment'),
    path('affirmations/<int:affirmation_id>/like/', toggle_affirmation_like, name='toggle_affirmation_like'),
    path('affirmations/saved/', saved_affirmations, name='saved_affirmations'),
    

    path('relaxation/', relaxation_list, name='relaxation_list'),
    path('relaxation/<slug:technique_slug>/', relaxation_detail, name='relaxation_detail'),

    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
