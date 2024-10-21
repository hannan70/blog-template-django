from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "comment_content": "Write Text",
            "username": "Your Name",
            "email": "Your Email"
        }
        error_messages = {
            "comment_content": {
                "required": "Comment field must not be empty"
            },
            "username": {
                "required": "Name field must not be empty"
            },
            "email": {
                "required": "Email field must not be empty"
            },
        }
        widgets = {
            "comment_content": forms.Textarea(attrs={"placeholder": "Write Comment", "rows": 5})
        }



