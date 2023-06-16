from .models import Comment, Scam
from django import forms

# Create a form for Comments from the model


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

# Create a form for scams from the model


class ScamForm(forms.ModelForm):
    class Meta:
        model = Scam
        fields = ('title', 'media', 'excerpt', 'content',)
