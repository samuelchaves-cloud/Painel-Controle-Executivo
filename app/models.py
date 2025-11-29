from django.db import models

# Create your models here.
from django.db import models

class Arquiteto(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    especialidade = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    #endereco = models.CharField(max_length=200)
    telefone_principal = models.CharField(max_length=20)
    telefone_secundario = models.CharField(max_length=20, blank=True)
    nome_secundario = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    TIPO_IMOVEL = [('Residência', 'Residência'), ('Condomínio', 'Condomínio'), ('Outro', 'Outro')]
    tipo_imovel = models.CharField(max_length=20, choices=TIPO_IMOVEL)
    nome_condominio = models.CharField(max_length=100, blank=True)
    nome_estabelecimento = models.CharField(max_length=100, blank=True)
    
    cep = models.CharField(max_length=9, blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.nome

class Visita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    arquiteto = models.ForeignKey(Arquiteto, on_delete=models.CASCADE)
    data_visita = models.DateTimeField()
    local = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    TIPO_IMOVEL = [('Residência', 'Residência'), ('Condomínio', 'Condomínio'), ('Outro', 'Outro')]
    STATUS = [('Agendada', 'Agendada'), ('Realizada', 'Realizada'), ('Cancelada', 'Cancelada')]
    status = models.CharField(max_length=20, choices=STATUS)
    observacoes = models.TextField(blank=True)

    ##def __str__(self):
    ##    return self.nome
    def __str__(self):
        return f"Visita em {self.local} - {self.status}"



class Obra(models.Model):
    Obra = models.CharField(max_length=500 , default="ADCIONE O NOME DA OBRA")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    arquiteto = models.ForeignKey(Arquiteto, on_delete=models.CASCADE)
    tipo_servico = models.CharField(max_length=300)
    valor_contrato = models.DecimalField(max_digits=10, decimal_places=2)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    STATUS_OBRA = [('Em andamento', 'Em andamento'), ('Concluída', 'Concluída'), ('Pausada', 'Pausada')]
    status = models.CharField(max_length=20, choices=STATUS_OBRA)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.Obra

class Pagamento(models.Model):
    #Obra = models.ForeignKey(Obra, on_delete=models.CASCADE, default = 1)
    #Obra = models.ForeignKey(Obra, on_delete=models.CASCADE, null=True, blank=True)
    Nome_Obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    #cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    parcelas_pendentes = models.IntegerField()
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2)
    proxima_vencimento = models.DateField()
    STATUS_PAGAMENTO = [('Em dia', 'Em dia'), ('Atrasado', 'Atrasado'), ('Quitado', 'Quitado')]
    status = models.CharField(max_length=20, choices=STATUS_PAGAMENTO)

    '''def __str__(self):
        return self.Nome_Obra'''

