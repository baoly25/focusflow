from django.db import models
from django.contrib.auth.models import User

class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journals')
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title







class StressTip(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    liked_by = models.ManyToManyField(User, related_name='liked_tips', blank=True)

    def __str__(self):
        return self.title

class TipComment(models.Model):
    tip = models.ForeignKey(StressTip, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 

class Affirmation(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    liked_by = models.ManyToManyField(User, related_name='liked_affirmations', blank=True)

    def __str__(self):
        return self.title

class AffirmationComment(models.Model):
    affirmation = models.ForeignKey(Affirmation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)










class RelaxationTechnique(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
