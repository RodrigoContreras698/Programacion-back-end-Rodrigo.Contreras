from django import forms
from reservasAPP.models import reserva
from django.core import validators

class FormProyecto(forms.ModelForm):
    class Meta:
        model = reserva
        fields = '__all__'

