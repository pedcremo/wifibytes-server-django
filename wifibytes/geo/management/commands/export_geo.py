# -*- coding: utf-8 -*-
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from geo.models import Pais, Provincia
from django.conf import settings
from datetime import datetime
from django.utils.dateformat import format
from wifibytes.export_functions import export_model
import csv
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Class MUST be named 'Command'


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (make_option(
        '--myoption', action='store', dest='myoption', default='default',
        help='Option help message'),)

    def handle(self, *app_labels, **options):

        start_time = int(format(datetime.now(), u'U'))

        print "Importando Paises"
        paises = Pais.objects.all()
        export_fields = ['codpais', 'codiso', 'nombre']
        destination_fields = ['codpais', 'codiso', 'nombre']

        export_model(export_fields, destination_fields, paises, 'paises')

        print "%s paises exportados - %s segundos" % (
            paises.count(), int(format(datetime.now(), u'U')) - start_time)

        print "Importando provincias"
        phase_time = int(format(datetime.now(), u'U'))
        provincias = Provincia.objects.all()
        export_fields = ['provincia', 'idprovincia', 'codpais', 'codigo']
        destination_fields = [
            'provincia', 'idprovincia', 'codpais', 'codigo']

        export_model(
            export_fields, destination_fields, provincias, 'provincias')

        print "%s provincias exportadas - %s segundos" % (
            provincias.count(),
            int(format(datetime.now(), u'U')) - phase_time)

        return u"Exportación finalizada - %s segundos" % (
            int(format(datetime.now(), u'U')) - start_time)
