from django import forms
from .models import Central

class ControllerForm(forms.ModelForm):

    class Meta:

        model = Central
        fields = ['ip_address', 'phase_value']
        widgets = {
            'ip_address': forms.TextInput(attrs={'class': 'form-control'}),
            'phase_value': forms.Select(attrs={'class': 'form-control'}),
        }
