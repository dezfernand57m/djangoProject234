from django import forms
from .models import User, Fileu


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class FileuForm(forms.ModelForm):
    class Meta:
        model = Fileu
        fields = '__all__'