from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View, generic
from django.shortcuts import redirect, render
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .forms import CustomUserCreationForm, ProfileForm # type: ignore
from profiles.models import Profile

class EmailDomainValidator:
    def __init__(self, allowed_domain):
        self.allowed_domain = allowed_domain

    def __call__(self, value):
        if not value.endswith(f'@{self.allowed_domain}'):
            raise ValidationError(f'Only email addresses from {self.allowed_domain} are allowed.')

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "You have successfully signed up and logged in.")
        return valid

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "You have successfully logged in.")
        return response

class CustomLogoutView(View):
    def get(self, request):
        return render(request, 'accounts/logout_confirm.html')

    def post(self, request):
        logout(request)
        messages.success(request, "You have been successfully logged out.")
        return redirect('home')

class ProfileView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.profile

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        messages.success(self.request, 'Your profile has been updated successfully.')
        return super().form_valid(form)