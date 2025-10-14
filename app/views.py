##from django.shortcuts import render

# Create your views here.


import requests
from django.http import JsonResponse

def buscar_cep(request):
    cep = request.GET.get('cep')
    if cep:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 200:
            data = response.json()
            if 'erro' not in data:
                return JsonResponse({
                    'endereco': data.get('logradouro', ''),
                    'bairro': data.get('bairro', ''),
                    'cidade': data.get('localidade', ''),
                    'estado': data.get('uf', '')
                })
    return JsonResponse({'error': 'CEP inválido'}, status=400)


from .forms import ClienteForm
from django.shortcuts import render

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()
    return render(request, 'cliente/cliente_form.html', {'form': form})
