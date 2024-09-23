from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from profiles.models import Profile

class EmailDomainValidator:
    def __init__(self, allowed_domain):
        self.allowed_domain = allowed_domain

    def __call__(self, value):
        if not value.endswith(f'@{self.allowed_domain}'):
            raise ValidationError(f'Only email addresses from {self.allowed_domain} are allowed.')

class CustomUserCreationForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Enter a valid email address.',
        validators=[EmailDomainValidator('factorypm.com')]
    )
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture', 'website']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }