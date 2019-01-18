# encoding:utf-8
from django.db import models
from tinymce.models import HTMLField


class Omv(models.Model):
    nombre = models.CharField(verbose_name=("Nombre"), max_length=100)
    descripcion = models.CharField(
        verbose_name=("Descripción"), max_length=500)
    codigo = models.IntegerField(
        primary_key=True, verbose_name=("Codigo"), editable=False)
    activo = models.BooleanField(
        verbose_name=("Activo"), null=False, default=0)

    def __unicode__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.codigo:

            no = self.__class__.objects.count()

            if no == 0:
                self.codigo = 1
            else:
                self.codigo = self.__class__.objects.all().order_by(
                    "-codigo")[0].codigo + 1

        super(self.__class__, self).save(*args, **kwargs)


class UserApiOmv(models.Model):
    uid = models.IntegerField(
        primary_key=True, verbose_name=("UID"), editable=False)
    user_login = models.CharField(verbose_name=("User Login"), max_length=30)
    user_password = models.CharField(
        verbose_name=("User Password"), max_length=30)
    codigo_omv = models.ForeignKey(
        Omv, verbose_name=("Codigo OMV"), related_name='UserOmv_Omv',on_delete=models.PROTECT)

    def __unicode__(self):
        return str(self.uid)

    def save(self, *args, **kwargs):
        if not self.uid:

            no = self.__class__.objects.count()

            if no == 0:
                self.uid = 1
            else:
                self.uid = self.__class__.objects.all().order_by(
                    "-uid")[0].uid + 1

        super(self.__class__, self).save(*args, **kwargs)


class TypeCallApi(models.Model):
    tid = models.IntegerField(
        primary_key=True, verbose_name=("ID"), editable=False)
    nombre = models.CharField(verbose_name=("nombre"), max_length=120)

    def __unicode__(self):
        return str(self.nombre)

    def save(self, *args, **kwargs):
        if not self.tid:
            no = self.__class__.objects.count()
            if no == 0:
                self.tid = 1
            else:
                self.tid = self.__class__.objects.all().order_by(
                    "-tid")[0].tid + 1
        super(self.__class__, self).save(*args, **kwargs)


class CallApi(models.Model):
    trans_list = (
        (0, ('GET')),
        (1, ('POST')),
        (2, ('PUT')),
    )
    call_id = models.IntegerField(
        primary_key=True, verbose_name=("ID"), editable=False)
    codigo_omv = models.ForeignKey(
        Omv, verbose_name=("Codigo OMV"), related_name='UserOmv_CallApi',on_delete=models.PROTECT)
    typecall = models.ForeignKey(
        TypeCallApi, verbose_name=("Tipo de Call"), related_name='TypeCallApi_CallApi',on_delete=models.PROTECT)
    url = models.CharField(verbose_name=("url"), max_length=120)
    authfield = models.CharField(verbose_name=("authfield info"), max_length=120)
    trans_call = models.IntegerField(
        verbose_name=("Tipo de Transacción"), choices=trans_list, null=True, blank=True)

    def __unicode__(self):
        return str(self.typecall.nombre)

    def save(self, *args, **kwargs):
        if not self.call_id:
            no = self.__class__.objects.count()
            if no == 0:
                self.call_id = 1
            else:
                self.call_id = self.__class__.objects.all().order_by(
                    "-call_id")[0].call_id + 1
        super(self.__class__, self).save(*args, **kwargs)


class ParamCallApi(models.Model):
    id = models.IntegerField(
        primary_key=True, verbose_name=("ID"), editable=False)
    call_id = models.ForeignKey(
        CallApi, verbose_name=("Call OMV"), related_name='CallApi_ParamCallApi',on_delete=models.PROTECT)
    param_name = models.CharField(
        verbose_name=("param nombre"), max_length=120)
    requerido = models.BooleanField(
        verbose_name=("Requerido"), default=None, blank=False, null=False)

    def __unicode__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if not self.id:
            no = self.__class__.objects.count()
            if no == 0:
                self.id = 1
            else:
                self.id = self.__class__.objects.all().order_by(
                    "-id")[0].id + 1
        super(self.__class__, self).save(*args, **kwargs)


class ParamCallBackApi(models.Model):
    id = models.IntegerField(
        primary_key=True, verbose_name=("ID"), editable=False)
    call_id = models.ForeignKey(
        CallApi, verbose_name=("Call OMV"), related_name='CallApi_ParamCallBackApi',on_delete=models.PROTECT)
    param_name = models.CharField(
        verbose_name=("param nombre"), max_length=120)


    def __unicode__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if not self.id:
            no = self.__class__.objects.count()
            if no == 0:
                self.id = 1
            else:
                self.id = self.__class__.objects.all().order_by(
                    "-id")[0].id + 1
        super(self.__class__, self).save(*args, **kwargs)
