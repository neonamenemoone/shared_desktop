from django import forms
from .models import Central

class ControllerForm(forms.ModelForm):

    class Meta:
        model = Central
        fields = ['ip_address', 'phase_value']
