from django.urls import reverse_lazy
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import FormView

from user.models import User
from .forms import UserRegistrationForm


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
            messages.error(self.request, 'Passwords do not match, please try again')
            return super().form_invalid(form, *args, **kwargs)
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


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user:
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('login')
        else:
            messages.error(request, 'Your credentials are incorrect or have expired')
            return redirect('login')
    return render(request, 'login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('login')
