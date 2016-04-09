from django import forms
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User, Permission, Group
from django.forms.models import ModelForm
# from django.utils.datastructures import SortedDict
from django.utils.translation import ugettext, ugettext_lazy as _


# Cria o form de criação de users
class AddUserForm(forms.Form):
    error_messages = {
        'err_pass': _(u"A Palavra-passe não coincide."),
        'err_dup': _(u"Nome de utilizador já existente."),
        'err_email': _(u"Já existe um utilizador com este e-mail."),
        'required': _(u"Campo de preenchemento obrigatório."),
    }

    username = forms.CharField(max_length=30, label=_(u'Nome utilizador'), widget=forms.TextInput(
        attrs={'class': 'form-control input-sm medio required_form', 'autofocus': "autofocus"}))
    p_nome = forms.CharField(max_length=30, label=_(u'Primeiro Nome'),
                             widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form'}))
    u_nome = forms.CharField(required=False, max_length=30, label=_(u'Último Nome'),
                             widget=forms.TextInput(attrs={'class': 'form-control input-sm medio'}))
    e_mail = forms.EmailField(max_length=75, label=_(u'E-mail'),
                              widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form'}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-sm medio required_form'}),
                          max_length=128, label=_(u'Palavra-passe'))
    pwd_ack = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-sm medio required_form'}),
                              max_length=128, label=_(u'Confirmar Palavra-passe'))

    grupos = forms.ModelMultipleChoiceField(Group.objects.all(), label=_(u'Perfil'), widget=forms.SelectMultiple(
        attrs={'multiple class': 'form-control required_form'}))

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['err_dup'])

    def clean_e_mail(self):
        e_mail = self.cleaned_data["e_mail"]
        try:
            User.objects.get(email=e_mail)
        except User.DoesNotExist:
            return e_mail
        raise forms.ValidationError(self.error_messages['err_email'])

    def clean_pwd_ack(self):
        pwd = self.cleaned_data.get("pwd")
        pwd_ack = self.cleaned_data.get("pwd_ack")
        if pwd and pwd_ack and pwd != pwd_ack:
            raise forms.ValidationError(
                self.error_messages['err_pass'])
        return pwd_ack

    class Meta:
        model = User
        fields = ("username", "password", "email")
        pass


# Cria o form de criação de grupos
class AddGroupForm(forms.Form):
    error_messages = {
        'err_dup': _(u"Nome de grupo já existente."),
    }

    name = forms.CharField(max_length=80, \
                           label=_(u'Descrição'), \
                           widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form', \
                                                         'autofocus': "autofocus"}
                                                  )
                           )

    perm = forms.ModelMultipleChoiceField(queryset=Permission.objects.filter(content_type=500).order_by('content_type_id'), \
                                          label=_(u'Permissões'), widget=forms.SelectMultiple(attrs=
                                                                                              {
                                                                                                  'multiple class': 'form-control required_form', \
                                                                                                  "size": 15}
                                                                                              )
                                          )

    class Meta:
        model = Group
        pass

    def clean_name(self):
        name = self.cleaned_data["name"]
        try:
            Group.objects.get(name=name)
        except Group.DoesNotExist:
            return name
        raise forms.ValidationError(self.error_messages['err_dup'])


# Cria o form de edição de grupos
class EditGroupForm(ModelForm):
    error_messages = {
        'err_dup': _(u"Nome de grupo já existente."),
    }

    name = forms.CharField(max_length=80, \
                           label=_(u'Descrição'), \
                           widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form', \
                                                         'autofocus': "autofocus"}
                                                  )
                           )

    perm = forms.ModelMultipleChoiceField(queryset=Permission.objects.filter(content_type=500).order_by('name'), \
                                          label=_(u'Permissões'), widget=forms.SelectMultiple(attrs=
                                                                                              {
                                                                                                  'multiple class': 'form-control required_form', \
                                                                                                  "size": 15}
                                                                                              ))

    def __init__(self, listaPerm, name, *args, **kwargs):
        super(EditGroupForm, self).__init__(*args, **kwargs)
        self.fields['perm'].initial = Permission.objects.filter(id__in=[int(idPerm.id) for idPerm in listaPerm])
        self.name = name

    def clean_name(self):
        name = self.cleaned_data["name"]
        if self.name != name:
            try:
                Group.objects.get(name=name)
            except Group.DoesNotExist:
                return name
            raise forms.ValidationError(self.error_messages['err_dup'])
        else:
            return name

    class Meta:
        model = Group
        fields = ("name",)
        pass


# Ficha da ficha de grupos
class FichaGroupForm(ModelForm):
    name = forms.CharField(max_length=80, \
                           label=_(u'Descrição'), \
                           widget=forms.TextInput(attrs={'class': 'form-control input-sm medio', \
                                                         'disabled': "disabled"}
                                                  )
                           )

    perm = forms.ModelMultipleChoiceField(queryset=Permission.objects.filter(content_type=500).order_by('name'), \
                                          label=_(u'Permissões'), widget=forms.SelectMultiple(attrs=
                                                                                              {
                                                                                                  'multiple class': 'form-control', \
                                                                                                  "size": 15,
                                                                                                  "disabled": "disabled"}
                                                                                              ))

    def __init__(self, listaPerm, *args, **kwargs):
        super(FichaGroupForm, self).__init__(*args, **kwargs)
        self.fields['perm'].queryset = Permission.objects.filter(id__in=[int(idPerm.id) for idPerm in listaPerm])
        self.fields['perm'].initial = Permission.objects.filter(id__in=[int(idPerm.id) for idPerm in listaPerm])

    class Meta:
        model = Group
        fields = []


# Formulário para a edição do utilizador    
class EditUserForm(ModelForm):
    error_messages = {
        'err_pass': _(u"A Palavra-passe não coincide."),
        'err_dup': _(u"Nome de utilizador já existente."),
        'err_email': _(u"Já existe um utilizador com este e-mail."),
        'required': _(u"Campo de preenchimento obrigatório."),
    }

    username = forms.CharField(max_length=30, \
                               label=_(u'Nome utilizador'), \
                               widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form', \
                                                             'autofocus': "autofocus"}
                                                      )
                               )
    first_name = forms.CharField(max_length=30, \
                                 label=_(u'Primeiro Nome'), \
                                 widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form'}))
    last_name = forms.CharField(required=False, max_length=30, \
                                label=_(u'Último Nome'), \
                                widget=forms.TextInput(attrs={'class': 'form-control input-sm medio'}))
    email = forms.EmailField(max_length=75, \
                             label=_(u'E-mail'), \
                             widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form'}))

    grupos = forms.ModelMultipleChoiceField(Group.objects.all(), label=_(u'Perfil'), widget=forms.SelectMultiple(
        attrs={'multiple class': 'form-control required_form'}))

    def __init__(self, username, email, listaGupos, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.username = username
        self.email = email
        self.fields['grupos'].initial = Group.objects.filter(id__in=[int(idGroup.id) for idGroup in listaGupos])

    def clean_username(self):
        username = self.cleaned_data["username"]
        if self.username != username:
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError(self.error_messages['err_dup'])
        else:
            return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if self.email != email:
            try:
                User.objects.get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError(self.error_messages['err_email'])
        else:
            return email

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        pass


# Formulário para a ver a ficha do utilizador
class FichaUserForm(ModelForm):
    username = forms.CharField(max_length=30, \
                               label=_(u'Nome utilizador'), \
                               widget=forms.TextInput(attrs={'class': 'form-control input-sm medio', \
                                                             'disabled': "disabled"}
                                                      )
                               )
    first_name = forms.CharField(max_length=30, \
                                 label=_(u'Primeiro Nome'), \
                                 widget=forms.TextInput(attrs={'class': 'form-control input-sm medio', \
                                                               'disabled': "disabled"}
                                                        )
                                 )
    last_name = forms.CharField(required=False, \
                                max_length=30, \
                                label=_(u'Último Nome'), \
                                widget=forms.TextInput(attrs={'class': 'form-control input-sm medio', \
                                                              'disabled': "disabled"}
                                                       )
                                )
    email = forms.EmailField(max_length=75, \
                             label=_(u'E-mail'), \
                             widget=forms.TextInput(attrs={'class': 'form-control input-sm medio', \
                                                           'disabled': "disabled"}
                                                    )
                             )

    grupos = forms.ModelMultipleChoiceField(Group.objects.all(), label=_(u'Perfil'), widget=forms.SelectMultiple(
        attrs={'multiple class': 'form-control', 'disabled': "disabled"}))

    def __init__(self, listaGupos, *args, **kwargs):
        super(FichaUserForm, self).__init__(*args, **kwargs)
        self.fields['grupos'].queryset = Group.objects.filter(id__in=[int(idGroup.id) for idGroup in listaGupos])
        self.fields['grupos'].initial = Group.objects.filter(id__in=[int(idGroup.id) for idGroup in listaGupos])


class PasswordChangeFormReset(forms.Form):
    error_messages = {
        'password_mismatch': _(u"As passwords não coincidem."),
    }

    password1 = forms.CharField(label=_("Nova Password"),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control input-sm medio required_form'}))

    password2 = forms.CharField(label=_("Nova Password (novamente)"),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control input-sm medio required_form'}))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PasswordChangeFormReset, self).__init__(*args, **kwargs)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):

        self.user.set_password(self.cleaned_data["password1"])
        if commit:
            self.user.save()
        return self.user


class MeuPerfilForm(ModelForm):
    error_messages = {
        'err_pass': _(u"A Palavra-passe não coincide."),
        'err_dup': _(u"Nome de utilizador já existente."),
        'err_email': _(u"Já existe um utilizador com este e-mail."),
        'required': _(u"Campo de preenchimento obrigatório."),
        'password_mismatch': _(u"As palavra-passe não coincidem."),
        'password_incorrect': _(u"As palavra-passe não coincidem."),
    }

    username = forms.CharField(max_length=30, \
                               label=_(u'Nome utilizador'), \
                               widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form', \
                                                             'autofocus': "autofocus"}
                                                      )
                               )
    first_name = forms.CharField(max_length=30, \
                                 label=_(u'Primeiro Nome'), \
                                 widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form'}))
    last_name = forms.CharField(required=False, \
                                max_length=30, \
                                label=_(u'Último Nome'), \
                                widget=forms.TextInput(attrs={'class': 'form-control input-sm medio'}))
    email = forms.EmailField(max_length=75, \
                             label=_(u'E-mail'), \
                             widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-sm medio required_form'}), \
                               max_length=128, \
                               label=_(u'Palavra-passe atual'))

    password1 = forms.CharField(required=False, \
                                label=_("Palavra-passe"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control input-sm medio'}))

    password2 = forms.CharField(required=False, \
                                label=_("Palavra-passe (novamente)"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control input-sm medio'}))

    def __init__(self, username, email, userAtual, *args, **kwargs):
        super(MeuPerfilForm, self).__init__(*args, **kwargs)
        self.username = username
        self.email = email
        self.userAtual = userAtual

    def clean_password(self):
        password = self.cleaned_data["password"]
        if not self.userAtual.check_password(password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'])
        return password

    def clean_username(self):
        username = self.cleaned_data["username"]
        if self.username != username:
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError(self.error_messages['err_dup'])
        else:
            return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if self.email != email:
            try:
                User.objects.get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError(self.error_messages['err_email'])
        else:
            return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        # print "OLAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        self.userAtual.set_password(self.cleaned_data["password1"])
        if commit:
            if len(str(self.cleaned_data["password1"])) > 0:
                self.userAtual.save()
        return self.userAtual

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")
        pass


class FichaMeuPerfilForm(ModelForm):
    username = forms.CharField(max_length=30, \
                               label=_(u'Nome utilizador'), \
                               widget=forms.TextInput(attrs={'class': 'form-control input-sm medio', \
                                                             'disabled': "disabled"}
                                                      )
                               )
    first_name = forms.CharField(max_length=30, \
                                 label=_(u'Primeiro Nome'), \
                                 widget=forms.TextInput(attrs={'class': 'form-control input-sm medio', \
                                                               'disabled': "disabled"}
                                                        )
                                 )
    last_name = forms.CharField(required=False, \
                                max_length=30, \
                                label=_(u'Último Nome'), \
                                widget=forms.TextInput(attrs={'class': 'form-control input-sm medio', \
                                                              'disabled': "disabled"}
                                                       )
                                )
    email = forms.EmailField(max_length=75, \
                             label=_(u'E-mail'), \
                             widget=forms.TextInput(attrs={'class': 'form-control input-sm medio', \
                                                           'disabled': "disabled"}
                                                    )
                             )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
