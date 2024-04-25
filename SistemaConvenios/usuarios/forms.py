from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confrima Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre(s)")
    last_name = forms.CharField(label="Apellido Paterno")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'first_name', 'last_name']
        help_texts = {k: "" for k in fields}


class AgregarUsuarioAGrupo(forms.Form):
    groups = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label="Sin permisos",
        required=False,
    )

    class Meta:
        model = User
        fields = ['groups']

    def save(self, user, commit=True):
        groups = self.cleaned_data.get('groups')
        user.groups.set([groups])
        if commit:
            user.save()
        return user
