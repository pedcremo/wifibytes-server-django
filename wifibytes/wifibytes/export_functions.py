# encoding:utf-8
from rest_framework import pagination
from django.conf import settings
import os
import csv


def export_model(export_fields, destination_fields, model, name):

    try:
        os.mkdir(os.path.join(settings.MEDIA_URL, 'csv'))
        os.mkdir(os.path.join(settings.MEDIA_URL + 'csv', 'to_export'))
    except Exception as msg:
        pass

    outfile_path = os.path.join(
        settings.MEDIA_URL, 'csv', "to_export/%s.csv" % name)

    outfile = open(outfile_path, 'wb')
    writer = csv.writer(outfile)
    writer.writerow(destination_fields)

    for row in model:
        to_write = []
        for v in export_fields:
            value = getattr(row, v)
            try:
                value = value.pk
            except Exception as msg:
                pass
            to_write.append(value)

        writer.writerow(to_write)
    outfile.close()
