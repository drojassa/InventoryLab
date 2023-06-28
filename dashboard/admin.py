from django.contrib import admin
from .models import Material, Pedido


admin.site.site_header= 'InventarioLab'

class MaterialAdmin(admin.ModelAdmin):
    list_display=('name', 'category', 'quantity')
    list_filter = ['category']
# Register your models here.
admin.site.register(Material,MaterialAdmin)
admin.site.register(Pedido)
