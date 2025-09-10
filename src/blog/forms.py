from django import forms
from .models import Comment
from .models import Post

class CommentForm(forms.ModelForm):

    class Meta:
        exclude = ["post"]
        model = Comment
        labels = {
            "username":"Your Name",
            "email":"Your Email",
            "text":"Your Comment",
        }