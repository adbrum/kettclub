from django import forms
from django.core.exceptions import ValidationError


class EmailForm(forms.Form):
    name = forms.CharField(label='Nome', widget=forms.TextInput(
        attrs={'placeholder': 'Nome', 'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control'}))
    phone = forms.CharField(label='Telefone', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Telefone', 'class': 'form-control'}))
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(
        attrs={'placeholder': 'Mensagem', 'class': 'form-control', 'rows': '5'}))

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        self.cleaned_data = super().clean()
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')

        return self.cleaned_data



# class EmailForm(forms.ModelForm):
#     class Meta:
#         model = Email
#         fields = ['name', 'email', 'phone', 'message']
#
#     def clean_name(self):
#         name = self.cleaned_data['name']
#         words = [w.capitalize() for w in name.split()]
#         return ' '.join(words)
#
#     def clean(self):
#         self.cleaned_data = super().clean()
#         if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
#             raise ValidationError('Informe seu e-mail ou telefone.')
#
#         return self.cleaned_data