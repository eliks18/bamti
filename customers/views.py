from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
# @login_required(login_url='login/', redirect_field_name='')
def create(request):
    form = forms.CreateCustomerForm()
    return render(request, "customers/create.html", {'form': form})
