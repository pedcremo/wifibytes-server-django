from django.contrib import admin
from .models import Empresa
# Register your models here.


class EmpresaAdmin(admin.ModelAdmin):
    model = Empresa

    list_display = (
        'direccion', 'web',
        'fax', 'email',
        'cifnif',
        'provincia', 'nombre', 'telefono', 'codpostal', 'ciudad'
    )

    fieldsets = (
        ('Informacion de la Empresa', {
            'fields': (
                'nombre',
                'cifnif',
                'email',
                'telefono',
                'fax'
            ),
        }),
        ('Informacion de localizacion', {
            'fields': (
                'codpostal',
                'ciudad',
                'provincia',
                'direccion'
            ),
        }),
    )


admin.site.register(Empresa, EmpresaAdmin)
