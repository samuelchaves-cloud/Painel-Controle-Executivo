from django.contrib import admin

admin.site.site_header = "Painel de Controle Canaã"
admin.site.site_title = "Painel de Controle"
admin.site.index_title = "Bem-vindo ao painel"


from.models import Arquiteto

@admin.register(Arquiteto)
class Arquitetoadmin(admin.ModelAdmin):
    list_display = ('nome','especialidade','telefone','email')
    search_fields = ['nome']



from.models import Cliente

@admin.register(Cliente)
class clienteadmin(admin.ModelAdmin):
    list_display = ('nome','telefone_principal','tipo_imovel')
    search_fields = ['nome']

from.models import Visita

@admin.register(Visita)
class visitaadmin(admin.ModelAdmin):
    list_display = ('cliente','arquiteto','data_visita','status')
    search_fields = ['cliente']

from.models import Obra

@admin.register(Obra)
class obraadmin(admin.ModelAdmin):
    list_display = ('Obra','status','cliente','valor_contrato')
    search_fields = ['Obra']



from.models import Pagamento

class StatusPagamentoFilter(admin.SimpleListFilter):
    title = 'Status do Pagamento'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        valores = Pagamento.objects.values_list('status', flat=True).distinct()
        return [(valor, valor) for valor in valores if valor]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())
        return queryset

# Admin com filtro ajustado
@admin.register(Pagamento)
class Pagamentoadmin(admin.ModelAdmin):
    list_display = ('Nome_Obra', 'status', 'cliente', 'parcelas_pendentes', 'valor_total')
    search_fields = ['Nome_Obra__Obra']  # busca pelo nome da obra
    list_filter = (StatusPagamentoFilter,)  # usa o filtro customizado