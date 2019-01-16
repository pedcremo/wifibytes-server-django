from django.db import models
from datetime import datetime
from django.utils.dateformat import format
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from cliente.models import MobilsClients


class RangoICC(models.Model):
    rango_icc_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    rango_icc_init = models.BigIntegerField(
        default=0, verbose_name='Rango Inicial',
        validators=[MaxValueValidator(999999999999999999), MinValueValidator(0)]
    )
    rango_icc_end = models.BigIntegerField(
        default=0, verbose_name='Rango Final',
        validators=[MaxValueValidator(999999999999999999), MinValueValidator(0)]
    )
    rango_icc_activo = models.BooleanField(default=False, verbose_name='Rango Activo')
    updated_at = models.IntegerField(default=0, editable=False)
    created_at = models.IntegerField(default=0, editable=False)

    @property
    def nuevo_icc_a_registrar(self):
        # Devuelve un icc nuevo a registrar
        return min(self.icc_disponibles)

    @property
    def icc_disponibles(self):
        icc_registrados = MobilsClients.objects.values_list('nuevoicc', flat=True)
        lst_disponibles = list(range(self.rango_icc_init, self.rango_icc_end))
        for icc in icc_registrados:
            if icc:
                icc = int(icc) / 10
                if icc in lst_disponibles:
                    lst_disponibles.remove(icc)
        return lst_disponibles

    @property
    def icc_registrados(self):
        icc_registrados = MobilsClients.objects.values_list('nuevoicc', flat=True)
        lst_disponibles = list(range(self.rango_icc_init, self.rango_icc_end))
        lst_registrados = []
        for icc in icc_registrados:
            if icc:
                icc = int(icc) / 10
                if icc in lst_disponibles:
                    lst_registrados.append(icc)
        return lst_registrados

    def __unicode__(self):
        return str(self.rango_icc_id)

    class Meta:
        verbose_name = 'Rango ICC'
        verbose_name_plural = 'Rangos ICC'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.updated_at = int(format(datetime.now(), 'U'))

        if not self.created_at:
            self.created_at = self.updated_at

        if self.rango_icc_activo:
            RangoICC.objects.all().update(rango_icc_activo=False)
            self.rango_icc_activo = True

        super(RangoICC, self).save(*args, **kwargs)
