from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label='Utilizador', widget=forms.TextInput(
        attrs={ 'class': 'form-text'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(
        attrs={'class': 'form-text'}))

# <div class="form-group form-animate-text" style="margin-top:40px !important;">
#                           <input type="text" class="form-text" required="">
#                           <span class="bar"></span>
#                           <label>TextBox</label>
#                         </div>