# encoding:utf-8

from django.contrib import admin
from omv.models import *
from catalogo.models import *
from django import forms
from django.conf import settings


class UserOmvInline(admin.StackedInline):
    model = UserApiOmv
    classes = ('collapse closed',)
    list_display = ('user_login', 'user_password')
    fields = ()
    extra = 0


class OmvAdmin(admin.ModelAdmin):
    inlines = [
        UserOmvInline,
    ]
    list_display = ('nombre', 'descripcion')


class ParamCallApiInline(admin.StackedInline):
    model = ParamCallApi
    classes = ('collapse closed', 'typecall', 'url')
    extra = 0


class ParamCallBackApiInline(admin.StackedInline):
    model = ParamCallBackApi
    classes = ('collapse closed', 'typecall', 'url')
    extra = 0


class CallApiAdmin(admin.ModelAdmin):
    inlines = [ParamCallApiInline, ParamCallBackApiInline]
    list_display = ('call_id', 'typecall')


# admin.site.register(CallApi, CallApiAdmin)
admin.site.register(Omv, OmvAdmin)
# admin.site.register(UserApiOmv)
