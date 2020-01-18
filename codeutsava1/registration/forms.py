from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2',
        'user_type']
    # name = forms.CharField(max_length=200)

class SellerForm(forms.Form):
    sell = forms.CharField(max_length=100)

# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
#
#
# class UserCreateForm(UserCreationForm):
#     class Meta:
#         fields = ("username", "email", "password1", "password2")
#         model = get_user_model()
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["username"].label = "Display name"
#         self.fields["email"].label = "Email address"
