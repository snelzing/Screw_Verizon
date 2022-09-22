from django import forms

from .models import Post, Email


class InputForm(forms.Form):
    screen_name = forms.CharField(required=True)

    # doing EmailInput makes the field not show up on the webpage
    email = forms.EmailField(required=True)



