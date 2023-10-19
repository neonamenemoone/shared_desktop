from django import forms
from .models import Central
import socket

def is_valid_ip(ip):
    try:
        socket.inet_pton(socket.AF_INET, ip)
        return True
    except socket.error:
        return False

class ControllerForm(forms.ModelForm):

    class Meta:

        model = Central
        fields = ['ip_address', 'phase_value']
        widgets = {
            'ip_address': forms.TextInput(attrs={'class': 'form-control'}),
            'phase_value': forms.Select(attrs={'class': 'form-control'}),
        }

class CustomControllerForm(ControllerForm):

    
    def clean_ip_address(self):
        ip_address = self.cleaned_data.get('ip_address')
        if not is_valid_ip(ip_address):
            raise forms.ValidationError("Invalid IP Address")
        return ip_address
