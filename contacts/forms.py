from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        labels = {
            "name": "Your Name",
            "email": "Your Email",
            "message": "Write Message",
        }
        error_messages = {
            "name": {
                "required": "Name field must not be empty",
            },
            "email": {
                "required": "Email field must not be empty",
            },
            "message": {
                "required": "Message field must not be empty",
            }
        }

