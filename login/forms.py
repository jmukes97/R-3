from django import forms
from .models import user

class signUp(forms.ModelForm):
    email = forms.EmailField(max_length=70)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = user
        fields = "__all__" 


