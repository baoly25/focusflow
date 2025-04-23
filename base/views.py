from .forms import SignUpForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from .forms import EmailAuthenticationForm
from django.shortcuts import render
from .models import Journal
from .forms import JournalForm
from django.contrib.auth.decorators import login_required
from .models import StressTip, TipComment
from .forms import TipCommentForm
from .models import Affirmation, AffirmationComment
from .forms import AffirmationCommentForm
from django.views.decorators.http import require_POST
from .forms import EditProfileForm
from .models import Task
from .forms import TaskForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    form = EmailAuthenticationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        auth_login(request, user)
        return redirect('home')
    return render(request, 'registration/login.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')

def pomodoro_timer(request):
    return render(request, 'pomodoro.html')

@login_required
def journal_list(request):
    journals = Journal.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'journal/list.html', {'journals': journals})

@login_required
def journal_create(request):
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.user = request.user
            journal.save()
            return redirect('journal_list')
    else:
        form = JournalForm()
    return render(request, 'journal/create.html', {'form': form})

@login_required
def journal_edit(request, pk):
    journal = get_object_or_404(Journal, pk=pk, user=request.user)
    if request.method == 'POST':
        form = JournalForm(request.POST, instance=journal)
        if form.is_valid():
            form.save()
            return redirect('journal_list')
    else:
        form = JournalForm(instance=journal)
    return render(request, 'journal/edit.html', {'form': form, 'journal': journal})

@login_required
def stress_tips_list(request):
    tips = StressTip.objects.all()
    return render(request, 'tips/list.html', {'tips': tips})

@login_required
@require_POST
def submit_tip_comment(request, tip_id):
    tip = get_object_or_404(StressTip, pk=tip_id)
    form = TipCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.tip = tip
        comment.user = request.user
        comment.save()
    return redirect('stress_tips')

@login_required
def toggle_tip_like(request, tip_id):
    tip = get_object_or_404(StressTip, pk=tip_id)

    if request.user in tip.liked_by.all():
        tip.liked_by.remove(request.user)
    else:
        tip.liked_by.add(request.user)

    referer = request.META.get('HTTP_REFERER')
    if referer and 'saved' in referer:
        return redirect('saved_tips')
    return redirect('stress_tips')

@login_required
def saved_tips(request):
    tips = request.user.liked_tips.all()
    return render(request, 'tips/saved.html', {'tips': tips})

@login_required
def affirmation_list(request):
    affirmations = Affirmation.objects.all()
    return render(request, 'affirmations/list.html', {'affirmations': affirmations})

@login_required
@require_POST
def submit_affirmation_comment(request, affirmation_id):
    affirmation = get_object_or_404(Affirmation, pk=affirmation_id)
    form = AffirmationCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.affirmation = affirmation
        comment.user = request.user
        comment.save()
    return redirect('affirmations')

@login_required
def toggle_affirmation_like(request, affirmation_id):
    affirmation = get_object_or_404(Affirmation, id=affirmation_id)

    if request.user in affirmation.liked_by.all():
        affirmation.liked_by.remove(request.user)
    else:
        affirmation.liked_by.add(request.user)

    referer = request.META.get('HTTP_REFERER')
    if referer and 'saved' in referer:
        return redirect('saved_affirmations')
    return redirect('affirmations')

@login_required
def saved_affirmations(request):
    affirmations = request.user.liked_affirmations.all()
    return render(request, 'affirmations/saved.html', {'affirmations': affirmations})

@login_required
@require_POST
def delete_affirmation_comment(request, comment_id):
    comment = get_object_or_404(AffirmationComment, id=comment_id, user=request.user)
    comment.delete()
    return redirect('affirmations')

@login_required
@require_POST
def delete_tip_comment(request, comment_id):
    comment = get_object_or_404(TipComment, id=comment_id, user=request.user)
    comment.delete()
    return redirect('stress_tips')

def relaxation_list(request):
    techniques = [
        {
            "name": "Deep Breathing",
            "slug": "deep-breathing",
            "image": "https://cdn.pixabay.com/photo/2023/06/15/01/37/nature-8064210_1280.png",
            "description": "A calming technique to regulate your breath and reduce anxiety."
        },
        {
            "name": "PMR",
            "slug": "pmr",
            "image": "https://cdn.pixabay.com/photo/2022/10/19/22/15/cat-7533717_1280.jpg",
            "description": "Progressive Muscle Relaxation relieves tension by tensing and relaxing each muscle group."
        },
        {
            "name": "Mindfulness Meditation",
            "slug": "meditation",
            "image": "https://cdn.pixabay.com/photo/2022/11/17/03/20/woman-7597270_1280.jpg",
            "description": "Focus on the present moment to ease your mind and body."
        }
    ]
    return render(request, 'relaxation/list.html', {'techniques': techniques})

def relaxation_detail(request, technique_slug):
    techniques = {
        "deep-breathing": {
            "title": "Deep Breathing",
            "sections": [
                {"label": "5 Minute Session", "youtube_url": "https://www.youtube.com/embed/j-1n3KJR1I8", "desc": "This video gently guides you through the 4-7-8 breathing method by inhaling for 4 seconds, hold for 7, and exhale for 8. It's a calming way to slow down, ease stress, and feel more centered."},
                {"label": "10 Minute Session", "youtube_url": "https://www.youtube.com/embed/LiUnFJ8P4gM", "desc": "This video leads you through a simple deep breathing exercise set to calming visuals and music. It's a peaceful way to reset your mind and relax your body."}
            ]
        },
        "pmr": {
            "title": "Progressive Muscle Relaxation",
            "sections": [
                {"label": "5 Minute Session", "youtube_url": "https://www.youtube.com/embed/5q3K-6HvQIk", "desc": "This video guides you through progressive muscle relaxation, helping you tense and release different muscle groups to ease physical tension. It's a calming way to reconnect with your body and reduce stress."},
                {"label": "15 Minute Session", "youtube_url": "https://www.youtube.com/embed/86HUcX8ZtAk", "desc": "This session walks you through progressive muscle relaxation with clear, steady instructions. It's designed to help you let go of built-up tension and feel more physically and mentally relaxed."}
            ]
        },
        "meditation": {
            "title": "Mindfulness Meditation",
            "sections": [
                {"label": "10 Minute Session", "youtube_url": "https://www.youtube.com/embed/6p_yaNFSYao", "desc": "This video offers a short mindfulness meditation focused on breathing and awareness. It's a simple way to slow down, stay present, and create a sense of calm."},
                {"label": "20 Minute Session", "youtube_url": "https://www.youtube.com/embed/-2zdUXve6fQ", "desc": "This guided meditation helps you center your attention and gently observe your thoughts. It's a quiet practice to build mindfulness and reduce mental clutter."}
            ]
        }
    }

    technique = techniques.get(technique_slug)
    if not technique:
        return redirect('relaxation_list')

    return render(request, 'relaxation/detail.html', {'technique': technique})

@login_required
@require_POST
def journal_delete(request, pk):
    journal = get_object_or_404(Journal, pk=pk, user=request.user)
    journal.delete()
    return redirect('journal_list')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user, completed=False).order_by('due_date')
    return render(request, 'tasks/list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create.html', {'form': form})

@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = True
    task.save()
    return redirect('task_list')

@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(user=request.user, completed=True).order_by('-due_date')
    return render(request, 'tasks/completed.html', {'tasks': tasks})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('task_list')

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit.html', {'form': form, 'task': task})

@login_required
@require_POST
def task_undo(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = False
    task.save()
    return redirect('completed_tasks')

@login_required
def user_settings(request):
    return render(request, 'settings.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_settings')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def progress_tracker(request):
    journal_count = Journal.objects.filter(user=request.user).count()
    completed_tasks = Task.objects.filter(user=request.user, completed=True).count()

    context = {
        'journal_count': journal_count,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'progress.html', context)