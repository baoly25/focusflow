from .forms import SignUpForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from .forms import EmailAuthenticationForm
from django.shortcuts import render
from .models import Journal
from .forms import JournalForm
from django.contrib.auth.decorators import login_required
from .models import StressTip, TipLike, TipComment
from .forms import TipCommentForm
from .models import Affirmation, AffirmationComment
from .forms import AffirmationCommentForm
from django.views.decorators.http import require_POST
from django.shortcuts import redirect


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
    tips = StressTip.objects.all().order_by('-id')
    liked_tip_ids = TipLike.objects.filter(user=request.user).values_list('tip_id', flat=True)
    return render(request, 'tips/list.html', {
        'tips': tips,
        'liked_tip_ids': liked_tip_ids,
        'comment_form': TipCommentForm()
    })

@login_required
def toggle_tip_like(request, tip_id):
    tip = get_object_or_404(StressTip, id=tip_id)
    like, created = TipLike.objects.get_or_create(user=request.user, tip=tip)
    if not created:
        like.delete()  # if already liked, unlike
    return redirect('stress_tips')

@login_required
def submit_tip_comment(request, tip_id):
    tip = get_object_or_404(StressTip, id=tip_id)
    if request.method == 'POST':
        form = TipCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.tip = tip
            comment.save()
    return redirect('stress_tips')

@login_required
def saved_tips(request):
    tips = StressTip.objects.filter(tiplike__user=request.user)
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
    return redirect('affirmations')  # Redirects back to the list page

@login_required
def saved_affirmations(request):
    affirmations = request.user.liked_affirmations.all()
    return render(request, 'affirmations/saved.html', {'affirmations': affirmations})

def relaxation_list(request):
    techniques = [
        {
            "name": "Deep Breathing",
            "slug": "deep-breathing",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_ZPuL7At42tM868IvRLZq-w40Uls7Fq9WXg&s?text=Deep+Breathing",
            "description": "A calming technique to regulate your breath and reduce anxiety."
        },
        {
            "name": "Progressive Muscle Relaxation",
            "slug": "pmr",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_ZPuL7At42tM868IvRLZq-w40Uls7Fq9WXg&s?text=PMR",
            "description": "Relieve tension by tensing and relaxing each muscle group."
        },
        {
            "name": "Mindfulness Meditation",
            "slug": "meditation",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_ZPuL7At42tM868IvRLZq-w40Uls7Fq9WXg&s?text=Meditation",
            "description": "Focus on the present moment to ease your mind and body."
        }
    ]
    return render(request, 'relaxation/list.html', {'techniques': techniques})

def relaxation_detail(request, technique_slug):
    techniques = {
        "deep-breathing": {
            "title": "Deep Breathing",
            "sections": [
                {"label": "5 Minute Session", "youtube_url": "https://www.youtube.com/embed/j-1n3KJR1I8", "desc": "description.........."},
                {"label": "10 Minute Session", "youtube_url": "https://www.youtube.com/embed/LiUnFJ8P4gM", "desc": "description.........."}
            ]
        },
        "pmr": {
            "title": "Progressive Muscle Relaxation",
            "sections": [
                {"label": "5 Minute Session", "youtube_url": "https://www.youtube.com/embed/5q3K-6HvQIk", "desc": "description.........."},
                {"label": "15 Minute Session", "youtube_url": "https://www.youtube.com/embed/86HUcX8ZtAk", "desc": "description.........."}
            ]
        },
        "meditation": {
            "title": "Mindfulness Meditation",
            "sections": [
                {"label": "10 Minute Session", "youtube_url": "https://www.youtube.com/embed/6p_yaNFSYao", "desc": "description.........."},
                {"label": "20 Minute Session", "youtube_url": "https://www.youtube.com/embed/-2zdUXve6fQ", "desc": "description.........."}
            ]
        }
    }

    technique = techniques.get(technique_slug)
    if not technique:
        return redirect('relaxation_list')

    return render(request, 'relaxation/detail.html', {'technique': technique})
