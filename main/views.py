from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from main.forms import InputForm

from .models import Post

# The createView is what actually renders the form


class HomePageView(FormView):
    template_name = "home.html"
    form_class = InputForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)


class ThanksPageView(TemplateView):
    template_name = "thanks.html"




