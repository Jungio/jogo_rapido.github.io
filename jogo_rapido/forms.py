from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Comentario


class NovoUsuarioForm(UserCreationForm):
 email = forms.EmailField()
 first_name = forms.CharField(max_length=150)
 last_name = forms.CharField(max_length=150)
 class Meta:
  model = User
  fields=['username', 'first_name', 'last_name','email', 'password1', 'password2']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto', 'estrelas']
        widgets = {
            'texto': forms.Textarea(attrs={'placeholder': 'Digite seu comentário aqui...', 'rows': 4}),
            'estrelas': forms.Select()
        }

        
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']