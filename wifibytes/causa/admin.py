# encoding:utf-8
from django.contrib import admin
from .models import *
from django import forms
from django.conf import settings
from django.forms import ModelForm
from suit.widgets import EnclosedInput



class CausaForm(ModelForm):
    class Meta:
        widgets = {
            'recaudacion' : EnclosedInput(append='&euro;')
        }

class CausaAdmin(admin.ModelAdmin):

    form = CausaForm

    def formatted_amount(self, obj):
        return '%.2f€' % obj.recaudacion

    formatted_amount.short_description = 'Recaudacion'
    formatted_amount.admin_order_field = 'recaudacion'

    list_display = ('fechainicio','nombre', 'activo', 'visible', 'formatted_amount')
    model = Causa

    list_filter = ('fechainicio', 'activo')


admin.site.register(Causa,CausaAdmin)
