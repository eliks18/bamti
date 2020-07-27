from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    """Definir campos, propiedades y estilos
    para el formulario de Login"""

    username = forms.CharField(
        required=True,
        label='Usuario T24',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-2'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-2'}
        ),
        required=True,
        label='Contraseña T24',
    )

    # def __init__(self, *args, **kwargs):
    #     super(LoginForm, self).__init__(*args, **kwargs)

    #     self.base_fields['username'].widget.attrs['class'] = 'form-control'
    #     self.base_fields['username'].widget.attrs['placeholder'] = 'Username'

    #     self.base_fields['password'].widget.attrs['class'] = 'form-control'
    #     self.base_fields['password'].widget.attrs['placeholder'] = 'Password'
        
    # class Meta():
    #     fields = ['usuario', 'contrasenia']
        # error_messages = {
        #     NON_FIELD_ERRORS: {
        #         "idk wtf am i doing",
        #     }
        # }
