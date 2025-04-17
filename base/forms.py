from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django import forms
from .models import Journal
from .models import TipComment
from .models import AffirmationComment

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'yourEmail@domain.com',
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            try:
                from django.contrib.auth.models import User
                username = User.objects.get(email=email).username
            except User.DoesNotExist:
                raise forms.ValidationError('No user with that email.')
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('Incorrect password.')
            self.user = user
        return self.cleaned_data

    def get_user(self):
        return self.user

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your thoughts here...'}),
        }

class TipCommentForm(forms.ModelForm):
    class Meta:
        model = TipComment
        fields = ['text']

class AffirmationCommentForm(forms.ModelForm):
    class Meta:
        model = AffirmationComment
        fields = ['text']








from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'notes', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Task Title'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Additional notes...'}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
