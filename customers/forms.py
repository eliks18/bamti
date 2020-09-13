from django import forms
# from django.contrib.auth.forms import AuthenticationForm

class CreateCustomerForm(forms.Form):
	CHOICES= (
		('','Elige una opción'),
		('1', 'Persona Física'),
		('2', 'Persona Física con Actividad Empresarial'),
		('3', 'Persona Moral'),
		)
	customer_type = forms.CharField(
		required = True,
		label = 'Tipo de Cliente *',
		widget = forms.Select(
			choices = CHOICES,
			attrs = {
            	'class': 'form-control',
            	'data-parsley-required-message': 'Este campo es obligatorio'
            }
		)
	)

	first_name  = forms.CharField(
		required = True,
		label = 'Primer Nombre *',
        widget = forms.TextInput(
            attrs = {
            	'class': 'form-control',
            	'data-parsley-required-message': 'Este campo es obligatorio'
            }
        )
	)
	second_name = forms.CharField(
		required = False,
		label = 'Segundo Nombre',
        widget = forms.TextInput(
            attrs = {'class': 'form-control'}
        )
    )
	third_name  = forms.CharField(
		required = False,
		label = 'Tercer Nombre',
        widget = forms.TextInput(
            attrs = {'class': 'form-control'}
        )
	)
	first_last_name  = forms.CharField(
		label = 'Apellido Paterno *',
        widget = forms.TextInput(
            attrs = {
            	'class': 'form-control',
            	'data-parsley-required-message': 'Este campo es obligatorio'
        	}
        )
	)
	second_last_name  = forms.CharField(
		label = 'Apellido Materno *',
        widget = forms.TextInput(
            attrs = {
            	'class': 'form-control',
            	'data-parsley-required-message': 'Este campo es obligatorio'
        	}
        )
	)
	birth_date  = forms.CharField(
		label = 'Fecha de Nacimiento *',
        widget = forms.TextInput(
            attrs = {
            	'class': 'form-control date',
            	'placeholder': 'dd/mm/yyyy',
            	'data-parsley-required-message': 'Este campo es obligatorio'
        	}
        )
	)
	rfc  = forms.CharField(
		label = 'RFC *',
        widget = forms.TextInput(
            attrs = {
            	'class': 'form-control date',
            	'data-parsley-required-message': 'Este campo es obligatorio'
        	}
        )
	)
	curp  = forms.CharField(
		label = 'CURP *',
        widget = forms.TextInput(
            attrs = {
            	'class': 'form-control date',
            	'data-parsley-required-message': 'Este campo es obligatorio'
        	}
        )
	)