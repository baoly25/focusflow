from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django import forms
from .models import Journal
from .models import TipComment

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
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Add a comment...',
            })
        }

from .models import AffirmationComment

class AffirmationCommentForm(forms.ModelForm):
    class Meta:
        model = AffirmationComment
        fields = ['text']
