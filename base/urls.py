from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import (
    register, login_view, homepage, pomodoro_timer,
    journal_list, journal_create, journal_edit,
    stress_tips_list, toggle_tip_like, submit_tip_comment, saved_tips,
    affirmation_list, submit_affirmation_comment,
    toggle_affirmation_like, saved_affirmations, relaxation_list,
    relaxation_detail, journal_delete, delete_affirmation_comment, delete_tip_comment,
    task_list, task_create, task_complete, completed_tasks, task_delete, task_edit, task_undo,
    user_settings, edit_profile,
    progress_tracker,
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
    path('tips/comment/<int:comment_id>/delete/', delete_tip_comment, name='delete_tip_comment'),

    # affirmations
    path('affirmations/', affirmation_list, name='affirmations'),
    path('affirmations/<int:affirmation_id>/comment/', submit_affirmation_comment, name='submit_affirmation_comment'),
    path('affirmations/<int:affirmation_id>/like/', toggle_affirmation_like, name='toggle_affirmation_like'),
    path('affirmations/saved/', saved_affirmations, name='saved_affirmations'),
    path('affirmations/comment/<int:comment_id>/delete/', delete_affirmation_comment, name='delete_affirmation_comment'),
    

    path('relaxation/', relaxation_list, name='relaxation_list'),
    path('relaxation/<slug:technique_slug>/', relaxation_detail, name='relaxation_detail'),
    
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

    # tasks
    path('tasks/', task_list, name='task_list'),
    path('tasks/new/', task_create, name='task_create'),
    path('tasks/<int:pk>/complete/', task_complete, name='task_complete'),
    path('tasks/completed/', completed_tasks, name='completed_tasks'),
    path('tasks/<int:pk>/delete/', task_delete, name='task_delete'),
    path('tasks/<int:pk>/edit/', task_edit, name='task_edit'),
    path('tasks/<int:pk>/undo/', task_undo, name='task_undo'),

    # settings
    path('settings/', user_settings, name='user_settings'),
    path('settings/edit-profile/', edit_profile, name='edit_profile'),
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name='change_password'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/change_password_done.html'), name='password_change_done'),

    # progress tracking
    path('settings/progress/', progress_tracker, name='progress_tracker'),
]
