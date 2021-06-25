from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import UserRegistrationForm
from user.models import User


class RegisterView(FormView):
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('register')

    def form_valid(self, form, *args, **kwargs):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']

        if password != confirm_password:
            messages.error(self.request, 'Password do not match, please try again')
        else:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )
            user.save()
        messages.success(self.request, 'Your account has been successfully created')
        return super().form_valid(form, *args, **kwargs)

    def form_invalid(self, form):
        messages.error(self.request, 'Something went wrong, try again')
        return super().form_invalid(form)
