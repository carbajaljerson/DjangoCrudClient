from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['razon_social','ruc','telefono','celular','contacto']
    search_fields = ['razon_social','ruc']
    #list_filter = ['razon_social']



# Register your models here.
admin.site.register(Cliente, ClienteAdmin)
