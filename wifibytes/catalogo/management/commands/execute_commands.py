# -*- coding: utf-8 -*-
import os

PATH_PROJECT = '/home/eric/GIT/wifibytes/Wifibytes/wifibytes-project/wifibytes'
PATH_VIRTUAL_ENV = '/home/eric/GIT/wifibytes/Wifibytes/bin/python'
PATH_MANAGE_PY = '/home/eric/GIT/wifibytes/Wifibytes/wifibytes-project/wifibytes/manage.py'
PATH_LOG = '/tmp/'
SETTINGS = 'wifibytes.settings.local'
LOG = False

TASKS = (
    'import_articles',
    'export_articles',
    'import_lineapedidos',
    'import_lineafacturas',
    'export_pedidos',
    'export_facturas',
    'export_lineafacturas',
    'export_lineapedidos',
)

for task in TASKS:
    CMD = task
    LOG_NAME = 'cronlog_' + CMD + '.txt'

    TASK = 'cd ' + PATH_PROJECT + ' && ' + PATH_VIRTUAL_ENV + ' ' + PATH_MANAGE_PY + ' ' + CMD + ' --myoption=default --settings='+SETTINGS
    if LOG:
        TASK += ' > ' + PATH_LOG+LOG_NAME + ' 2>&1'
    os.system(TASK)
