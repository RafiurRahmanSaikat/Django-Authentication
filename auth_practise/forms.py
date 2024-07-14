from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        # exclude = ["password"]
