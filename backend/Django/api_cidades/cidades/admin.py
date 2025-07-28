from django.contrib import admin
from django.utils.html import format_html

from .models import Estado, Cidade

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1 
    readonly_fields = ['dono'] 

'''
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla']
    inlines = [CidadeInline]
'''

class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla', 'preview_foto']
    inlines = [CidadeInline]

    def preview_foto(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="height:50px;" />', obj.foto.url)
        return "Sem imagem"
    preview_foto.short_description = 'Foto'

admin.site.register(Estado, EstadoAdmin)

class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'estado', 'dono']
    list_filter = ['estado']
    search_fields = ['nome']

admin.site.register(Cidade, CidadeAdmin)

