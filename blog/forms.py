from .models import Comment, Scam
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ScamForm(forms.ModelForm):
    class Meta:
        model = Scam
        fields = ('title', 'media', 'excerpt', 'content',)
