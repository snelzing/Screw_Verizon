from django import forms

from .models import Post


class InputForm(forms.Form):
    class Meta:
        model = Post
        fields = (
            "screen_name",
            "email",
        )
    name = forms.CharField()
    email = forms.EmailField()



