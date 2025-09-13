from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'cep': forms.TextInput(attrs={'id': 'cep'}),
            'endereco': forms.TextInput(attrs={'id': 'endereco'}),
            'bairro': forms.TextInput(attrs={'id': 'bairro'}),
            'cidade': forms.TextInput(attrs={'id': 'cidade'}),
            'estado': forms.TextInput(attrs={'id': 'estado'}),
        }
