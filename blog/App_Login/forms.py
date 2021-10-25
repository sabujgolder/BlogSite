from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class sign_up(UserCreationForm):
    email = forms.EmailField(required=False,label="Email Address")
    phone_no = forms.CharField(required = False,label = "Phone Number")
    class Meta:
        model = User
        fields = ('username','email','phone_no','password1','password2')
