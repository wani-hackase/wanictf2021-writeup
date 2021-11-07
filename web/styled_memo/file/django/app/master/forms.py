from app.forms import FormControlMixin
from app.master.models import User

from django import forms
from django.contrib.auth.forms import AuthenticationForm as DjangoAuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import FileExtensionValidator


class RegisterForm(FormControlMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)


class AuthenticationForm(FormControlMixin, DjangoAuthenticationForm):
    pass


class UserEditForm(FormControlMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["css"].widget.attrs["accept"] = ".css"
        self.fields["css"].validators.append(FileExtensionValidator(["css"]))

    class Meta:
        model = User
        fields = ("username", "css")
