# encoding:utf-8
from django.shortcuts import render, get_object_or_404
from cliente.models import MobilsClients
# from wifibytes.omv_functions import altaCliente, altaLinea, portabilidadLinea


# def activar_linea(request, id_linea):
#
#     activa = None
#     message = None
#     linea = get_object_or_404(MobilsClients, pk=id_linea)
#     if linea.codcliente:
#         cliente = linea.codcliente
#         if cliente.birthday_omv:
#             birthday = cliente.birthday_omv.strftime('%d/%m/%Y')
#         else:
#             birthday = None
#             activa = False
#             message = '%s <a href="/admin/cliente/cliente/%s/">%s</a>' % (
#                 'La fecha de nacimiento no es correcta',
#                 cliente.pk, 'Ver cliente')
#         if not cliente.cifnif_imageA:
#             birthday = None
#             activa = False
#             message = '%s <a href="/admin/cliente/cliente/%s/">%s</a>' % (
#                 u'El cliente no ha subido su documentación',
#                 cliente.pk, 'Ver cliente')
#     else:
#         cliente = None
#         activa = False
#         message = '%s <a href="/admin/cliente/mobilsclients/%s/">%s</a>' % (
#             'La línea no tiene ningún cliente asignado',
#             linea.pk, 'Ver línea')
#
#     params = {
#         "subscriberType": cliente.tipo_cliente,
#         "marketingConsent": cliente.newsletter,
#         "documentType": cliente.tipo_documento, "fiscalId": cliente.cifnif,
#         "name": cliente.nombre, "contactName": cliente.nombre,
#         "contactFamilyName1": cliente.apellido,
#         "contactFamilyName2": cliente.segundo_apellido,
#         "emailAddress": cliente.email, "contactPhone": cliente.telefono,
#         "birthday": birthday,
#         "documento": cliente.cifnif_imageA}
#
#     if linea.coddir:
#         params["addressRegion"] = (
#             linea.coddir.idprovincia.codcomunidad.nombre)
#         params["addressProvince"] = linea.coddir.idprovincia.provincia
#         params["addressCity"] = linea.coddir.ciudad
#         params["addressPostalCode"] = linea.coddir.codpostal
#         params["addressStreet"] = linea.coddir.direccion
#         params["addressNumber"] = linea.coddir.numero
#     else:
#         activa = False
#         message = '%s<a href="/admin/cliente/mobilsclients/%s/">%s</a>' % (
#             u'La línea no tiene ninguna dirección asignada ',
#             linea.pk, u'Ver línea')
#
#     if request.method == 'GET':
#
#         return render(request, 'activar_linea.html', {
#             'info': params, 'id_linea': id_linea, 'activa': activa,
#             'message': message})
#
#     elif request.method == "POST":
#
#         received = request.POST
#         if(linea.icc_anterior):
#             alta = portabilidadLinea(
#                 id_linea, received['icc'], received['dc'])
#         else:
#             alta = altaLinea(id_linea, received['icc'], received['dc'])
#
#         activa = False
#         message = alta['message']
#         if alta['response_code'] == '0001':
#             activa = True
#             linea.alta = True
#             linea.save()
#
#         return render(request, 'activar_linea.html', {
#             'info': params, 'id_linea': id_linea, 'activa': activa,
#             'message': message})
