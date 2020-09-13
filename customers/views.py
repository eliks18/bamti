from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from . import forms

# Create your views here.
# @login_required(login_url='login/', redirect_field_name='')
def create(request):
    form = forms.CreateCustomerForm()
    return render(request, "customers/create.html", {'form': form})

def validate_customer_type(request):
	customer_type = request.POST.get('customer_type', None)
	if customer_type == "1":
		# FISICA
		fields = {
			"Personal": {
				"first_name": {
					"required": True,
					"label": "Primer Nombre",
					"type": "input"
				},
				"second_name": {
					"required": False,
					"label": "Segundo Nombre",
					"type": "input"
				},
				"third_name": {
					"required": False,
					"label": "Tercer Nombre",
					"type": "input"
				},
				"first_lastname": {
					"required": True,
					"label": "Primer Apellido",
					"type": "input"
				},
				"second_lastname": {
					"required": True,
					"label": "Segundo Apellido",
					"type": "input"
				},
				"birth_date": {
					"required": True,
					"label": "Fecha de Nacimiento",
					"type": "input"
				},
				"rfc": {
					"required": True,
					"label": "RFC",
					"type": "input"
				},
				"curp": {
					"required": True,
					"label": "CURP",
					"type": "input"
				},
				"marital_status": {
					"required": True,
					"label": "Estado Civil",
					"type": "select",
					"options": {
						"1": "Soltero"
					}
				}
			}
		}
		return JsonResponse(fields, status=200)
		# return JsonResponse({"customer_type": customer_type}, status=200)
	elif customer_type == "2":
		# FISICA CON ACTIVIDAD EMPRESARIAL
		return JsonResponse({"customer_type": customer_type}, status=200)
	elif customer_type == "3":
		# MORAL
		return JsonResponse({"customer_type": customer_type}, status=200)
	else:
		return JsonResponse({"error": "invalid customer_type"}, status=404)
