# -*- coding: utf-8 -*-
''' Script que ejecuta todas las tareas '''
import os

PATH_PROJECT = '/home/eric/GIT/wifibytes/Wifibytes/wifibytes-project/wifibytes'

APPS_TASKS = (
    'catalogo',
    'cliente',
    'facturacion'
)

for task in APPS_TASKS:
    TASK = 'python ' + PATH_PROJECT + '/' + task + '/management/commands/execute_commands.py'
    os.system(TASK)
