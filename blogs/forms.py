from .models import BlogPost, Comment
from django import forms
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title','content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)