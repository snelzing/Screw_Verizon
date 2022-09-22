from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.shortcuts import redirect
from main.forms import InputForm

from .models import Post, Email

# The createView is what actually renders the form


class HomePageView(View):
    template_name = "home.html"

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        form = InputForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = InputForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})
        screen_name = form.cleaned_data['screen_name']
        email_str = form.cleaned_data['email']
        print(screen_name, email_str)
        email, created = Email.objects.get_or_create(email__iexact=email_str, defaults={'email': email_str})
        print(email)
        Post.objects.create(email=email, screen_name=screen_name)
        return redirect('thanks')


class ThanksPageView(TemplateView):
    template_name = "thanks.html"




