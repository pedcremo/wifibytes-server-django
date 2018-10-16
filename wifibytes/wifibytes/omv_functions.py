# encoding:utf-8
from django.conf import settings
from lxml import objectify, etree
from django.http import HttpResponseForbidden
#from cliente.models import MobilsClients, Cliente
from signaturit_sdk.signaturit_client import SignaturitClient

import xml.etree.ElementTree as ET

import urllib2
import string
import os
import sys
import httplib
import base64
from functools import wraps
import errno
import os
import signal
import time


def errorMessage(function, code):

    error_codes = {}

    error_codes['altaCliente'] = [
        {"code": "0001", "message": "OK"},
        {"code": "0002", "message": ("Usuario está vacío o es superior a 20 "
                                     "caracteres.")},
        {"code": "0003", "message": ("Contraseña está vacía o es superior a "
                                     "20 caracteres.")},
        {"code": "0004", "message": "El usuario no existe."},
        {"code": "0005", "message": "Contraseña no válida."},
        {"code": "0006", "message": "Error en la validación con el usuario."},
        {"code": "0007", "message": "Provincia indicada no válida."},
        {"code": "0008", "message": "Error al obtener la provincia."},
        {"code": "0009", "message": "Provincia de envío indicada no válida."},
        {"code": "0010", "message": "Error al obtener la provincia de envío."},
        {"code": "0011", "message": ("No hay archivo para el documento de "
                                     "identificación.")},
        {"code": "0012", "message": ("Formato incorrecto para el documento "
                                     "de identificación.")},
        {"code": "0013", "message": "Campo NIF/CIF/NIE incorrecto."},
        {"code": "0014", "message": ("Si el cliente es tipo empresa, campo "
                                     "razón social y los datos del apoderado "
                                     "deben de estar rellenos.")},
        {"code": "0015", "message": ("Si el tipo de cliente es empresa el "
                                     "documento debe de ser un CIF.")},
        {"code": "0016", "message": ("Si el tipo de cliente es residencial, "
                                     "autónomo o extranjero, el campo nombre y"
                                     " primer apellido no pueden estar "
                                     "vacíos")},
        {"code": "0017", "message": ("El documento para un cliente de tipo res"
                                     "idencial/autónomo/extranjero no es"
                                     "correcto.")},
        {"code": "0018", "message": ("El documento de identificación introduci"
                                     "do ya existe en el sistema.")},
        {"code": "0019", "message": ("La fecha de nacimiento introducida no es"
                                     " correcta.")},
        {"code": "0020", "message": "Error al insertar el nuevo usuario."},
        {"code": "0021", "message": "Error al insertar el nuevo usuario."},
        {"code": "0022", "message": "Error al subir el documento."},
        {"code": "0023", "message": ("No se han rellenado todos los datos "
                                     "personales obligatorios.")},
        {"code": "0024", "message": "La cuenta bancaria no es correcta."}
    ]

    error_codes['altaLinea'] = [
        {"code": "0001", "message": "OK"},
        {"code": "0002", "message": ("Usuario está vacío o es superior a 20 "
                                     "caracteres.")},
        {"code": "0003", "message": ("Contraseña está vacía o es superior a 20"
                                     " caracteres.")},
        {"code": "0004", "message": "El usuario no existe."},
        {"code": "0005", "message": "Contraseña no válida."},
        {"code": "0006", "message": "Error en la validación con el usuario."},
        {"code": "0007", "message": ("No se ha introducido la tarifa a la que "
                                     "asociar la línea.")},
        {"code": "0008", "message": "Error al obtener sus datos como agente."},
        {"code": "0009", "message": "Error al obtener sus datos como agente."},
        {"code": "0010", "message": "Error al obtener la tarifa."},
        {"code": "0011", "message": ("No existe ninguna tarifa para el tipo de"
                                     " cliente que ha insertado.")},
        {"code": "0012", "message": "Error al obtener los datos del cliente."},
        {"code": "0013", "message": ("No existe ningún cliente asociado con el"
                                     " NIF indicado.")},
        {"code": "0014", "message": ("ICC o Dígito de control no deben de "
                                     "estar vacíos.")},
        {"code": "0015", "message": "Teléfono no puede estar vacío."},
        {"code": "0016", "message": "ICC no es numérico."},
        {"code": "0017", "message": ("El número de la tarjeta SIM introducido "
                                     "no es correcto.")},
        {"code": "0018", "message": ("El número introducido de la tarjeta SIM "
                                     "no está aprovisionado.")},
        {"code": "0019", "message": ("El número introducido de la tarjeta SIM "
                                     "no corresponde al rango que usted tiene "
                                     "asignado.")},
        {"code": "0020", "message": ("La tarjeta SIM introducida ya está en "
                                     "uso en otra línea.")},
        {"code": "0021", "message": ("Para la tarifa seleccionada, debe "
                                     "introducir el teléfono asociado.")},
        {"code": "0022", "message": ("El teléfono asociado que ha introducido "
                                     "no pertenece a un teléfono suyo.")},
        {"code": "0023", "message": ("El teléfono asociado, ya tiene asociada "
                                     "una tarifa.")},
        {"code": "0024", "message": ("El formato del teléfono introducido no "
                                     "es correcto.")},
        {"code": "0025", "message": ("El número de teléfono introducido no "
                                     "está aprovisionado.")},
        {"code": "0026", "message": ("El teléfono introducido no corresponde a"
                                     " su rango.")},
        {"code": "0027", "message": ("El teléfono introducido ya está en uso "
                                     "por otra línea.")},
        {"code": "0028", "message": ("El teléfono introducido está en "
                                     "cuarentena.")},
        {"code": "0029", "message": ("No se encuentra el cliente en el "
                                     "sistema.")},
        {"code": "0030", "message": ("Error al insertar la solicitud de "
                                     "línea.")},
        {"code": "0031", "message": ("Error al insertar la solicitud de "
                                     "línea.")},
        {"code": "0032", "message": "No se ha podido aprovisionar la SIM."},
        {"code": "0033", "message": ("No se ha podido aprovisionar el número "
                                     "de teléfono.")},
        {"code": "0034", "message": ("El número seleccionado ha caducado su "
                                     "reserva de número.")},
        {"code": "0035", "message": ("El conjunto de bonos de Voz/Datos "
                                     "contiene más de un elemento.")},
        {"code": "0036", "message": ("El/Los bono/s no son compatibles con la"
                                     " tarifa seleccionada.")},
        {"code": "0037", "message": ("El bono de datos no asignado "
                                     "correctamente.")},
        {"code": "0038", "message": ("El bono de voz no asignado "
                                     "correctamente.")}
    ]

    error_codes['portabilidadLinea'] = [
        {"code": "0001", "message": "OK"},
        {"code": "0002", "message": ("Usuario está vacío o es superior a 20 "
                                     "caracteres.")},
        {"code": "0003", "message": ("Contraseña está vacía o es superior a 20"
                                     " caracteres.")},
        {"code": "0004", "message": "El usuario no existe."},
        {"code": "0005", "message": "Contraseña no válida."},
        {"code": "0006", "message": "Error en la validación con el usuario."},
        {"code": "0007", "message": ("No se ha introducido la tarifa a la que "
                                     "asociar la línea.")},
        {"code": "0008", "message": "Error al obtener sus datos como agente."},
        {"code": "0009", "message": "Error al obtener sus datos como agente."},
        {"code": "0010", "message": ("Error al obtener los datos de la "
                                     "tarifa.")},
        {"code": "0011", "message": ("No existe ninguna tarifa para el tipo de"
                                     " cliente que ha insertado.")},
        {"code": "0012", "message": "NIF introducido no válido."},
        {"code": "0013", "message": "Error al obtener los datos del cliente."},
        {"code": "0014", "message": ("No existe ningún cliente asociado con el"
                                     " NIF indicado.")},
        {"code": "0015", "message": ("ICC o Dígito de control no deben de "
                                     "estar vacíos.")},
        {"code": "0016", "message": "Teléfono no puede estar vacío."},
        {"code": "0017", "message": "El formato del teléfono no es válido."},
        {"code": "0018", "message": ("Modalidad de pago actual no puede estar "
                                     "vacía.")},
        {"code": "0019", "message": "Modalidad de pago actual no válida."},
        {"code": "0020", "message": "ICC no es numérico."},
        {"code": "0021", "message": ("El número de la tarjeta SIM introducido "
                                     "no es correcto.")},
        {"code": "0022", "message": ("El número introducido de la tarjeta SIM "
                                     "no está aprovisionado.")},
        {"code": "0023", "message": ("El número introducido de la tarjeta SIM "
                                     "no corresponde al rango que usted tiene "
                                     "asignado.")},
        {"code": "0024", "message": ("La tarjeta SIM introducida ya está en "
                                     "uso en otra línea.")},
        {"code": "0025", "message": ("Para la tarifa seleccionada, debe "
                                     "introducir el teléfono asociado.")},
        {"code": "0026", "message": ("El teléfono asociado que ha introducido "
                                     "no pertenece a un teléfono suyo.")},
        {"code": "0027", "message": ("El teléfono asociado, ya tiene asociada "
                                     "una tarifa.")},
        {"code": "0028", "message": ("Error al obtener sus solicitudes.")},
        {"code": "0029", "message": ("El teléfono indicado ya está insertado "
                                     "en el sistema.")},
        {"code": "0030", "message": ("No se encuentra el cliente en el "
                                     "sistema.")},
        {"code": "0031", "message": ("Error al insertar la solicitud de "
                                     "línea.")},
        {"code": "0032", "message": ("Número de tarjeta SIM donante no "
                                     "válido.")},
        {"code": "0033", "message": ("No se han insertado los datos de la "
                                     "portabilidad correctamente.")},
        {"code": "0034", "message": ("No se han insertado los datos de la "
                                     "portabilidad correctamente.")},
        {"code": "0035", "message": ("No se ha insertado la línea "
                                     "correctamente.")},
        {"code": "0036", "message": ("No se ha insertado la línea "
                                     "correctamente.")},
        {"code": "0037", "message": "No se ha podido aprovisionar la SIM."},
    ]

    error_codes['subirDocumento'] = [
        {"code": "0001", "message": "OK"},
        {"code": "0002", "message": ("Usuario está vacío o es superior a 20 "
                                     "caracteres.")},
        {"code": "0003", "message": ("Contraseña está vacía o es superior a 20"
                                     " caracteres.")},
        {"code": "0004", "message": "El usuario no existe."},
        {"code": "0005", "message": "Contraseña no válida."},
        {"code": "0006", "message": "Error en la validación con el usuario."},
        {"code": "0007", "message": "NIF del titular de la línea no correcto"},
        {"code": "0008", "message": ("El tipo de documento está vacío o no "
                                     "coincide con los tipos admitidos.")},
        {"code": "0009", "message": ("El código de la solicitud no puede estar"
                                     " vacío.")},
        {"code": "0010", "message": "Error al obtener datos del cliente."},
        {"code": "0011", "message": ("El NIF indicado no se encuentra en el "
                                     "sistema.")},
        {"code": "0012", "message": ("Error al encontrar la solicitud de la "
                                     "línea.")},
        {"code": "0013", "message": ("No se ha encontrado la solicitud de la "
                                     "línea.")},
        {"code": "0014", "message": "No ha subido un documento."},
        {"code": "0015", "message": "Extensión del documento no válida."},
        {"code": "0016", "message": "Error al subir el fichero."},
        {"code": "0017", "message": "Fichero subido correctamente."}
    ]

    error_codes['cancelLineasSolicitud'] = [
        {"code": "0001", "message": "Solicitud cancelada con éxito."},
        {"code": "0002",
         "message": "Usuario está vacío o es superior a 20 caracteres."},
        {"code": "0003",
         "message": "Contraseña está vacía o es superior a 20 caracteres."},
        {"code": "0004", "message": "El usuario no existe."},
        {"code": "0005", "message": "Contraseña no válida."},
        {"code": "0006", "message": "Error en la validación con el usuario."},
        {"code": "0007", "message":
         "Error al encontrar la solicitud de línea."},
        {"code": "0008", "message": "El código de solicitud no es correcto."},
        {"code": "0009",
         "message": "Error al obtener el estado de la solicitud."},
        {"code": "0010",
         "message": ("El estado de la solicitud no es el correcto para que "
                     "la solicitud sea cancelada.")},
        {"code": "0011", "message": "Error al cancelar la solicitud."},
        {"code": "0012",
         "message": ("El periodo para cancelar la solicitud de portabilidad "
                     "ha expirado.")},
        {"code": "0013", "message": "Error al cancelar la solicitud."},
        {"code": "0014", "message": "Error al cancelar la solicitud."},
        {"code": "0015", "message": "Error al cancelar la solicitud."}]

    return (
        item for item in error_codes[function] if item["code"] == code).next()


def makeCall(function, params):
    server_addr = settings.OMV_SERVER_ADDR
    user = settings.OMV_USER
    password = settings.OMV_PASSWORD

    print ('user', user)
    print ('password', password)

    service_action = "/ws_desarrollo/mv/gestMOVIL_2.php?WSLD"

    body = """<?xml version='1.0' encoding='UTF-8'?>
    <soapenv:Envelope xmlns:SOAP-ENV="http://
    schemas.xmlsoap.org/soap/envelope"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
    xmlns:tns="URN:IONMOBILEWS"
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns="http://schemas.xmlsoap.org/wsdl/"
    targetNamespace="URN:IONMOBILEWS">
    <soapenv:Header/>
    <soapenv:Body>
    <ns:%s>
    <ns:userInfo>
    <ns:user>%s</ns:user>
    <ns:pass>%s</ns:pass>""" % (function, user, password)
    for k, v in params.iteritems():
        body += u"<ns:%s>%s</ns:%s>" % (k, v, k)
    body += """
    </ns:userInfo>
    </ns:%s>
    </soapenv:Body>
    </soapenv:Envelope>""" % function

    body = body.encode('utf-8')

    print('\n----------------------------')
    print('   CALL [OMV] --> ')
    print('   [function]-->', function)
    print('   [params]-->', params)

    request = httplib.HTTPConnection(server_addr, timeout=30)
    request.putrequest("POST", service_action)
    request.putheader(
        "Accept",
        "application/soap+xml, application/dime, multipart/related, text/*")
    request.putheader("Content-Type", "text/xml; charset=utf-8")
    request.putheader("Cache-Control", "no-cache")
    request.putheader("Pragma", "no-cache")
    request.putheader("SOAPAction", "http://" + server_addr + service_action)
    request.putheader("Content-Length", str(len(body)))
    request.endheaders()
    request.send(body)
    response = request.getresponse()

    print('   [response]-->', response)
    # print(readResponse(response))
    print('----------------------------\n')
    return response


def readResponse(response):
    print("   [Leyendo respuesta] ...")
    try:
        root = ET.fromstring(response.read())
        print("     respuesta leida")
        print(root)
        return root[0]
    except:
        print('[ERROR] leyendo respuesta')
    return '[ERROR] leyendo response'


def getpool():
    params = {}
    response = makeCall("getPoolMsisdn", params)
    if response.status == 403:
        return {
            'status_code': 403
        }
    else:
        root = ET.fromstring(response.read())
        content = {}
        for a in root[0][0][0]:
            content[a.tag] = a.text

        return {
            'status_code': 200,
            'numbers': content
        }


def getpoolSim():
    params = {}
    response = makeCall("getPoolSIM", params)
    if response.status == 403:
        return {
            'status_code': 403
        }
    else:
        root = ET.fromstring(response.read())
        content = {}

        print('-----------------> GETPOOLSIM <----------------------')
        print(root)

        for a in root.iter():
            content[a.tag] = a.text

        return {
            'status_code': 200,
            'response': content
        }


def getCDR(mes, anyo, t_origen, tipo_servicio):

    params = {'mes': str(mes), 'anyo': int(anyo),
              'tipo_servicio': tipo_servicio, 't_origen': str(t_origen)}

    response = makeCall("getCDR", params)
    if response.status == 403:
        return {
            'status_code': 403
        }
    else:
        root = ET.fromstring(response.read())
        content = []
        for a in root[0][0][0]:
            dic = {}
            for e in a:
                dic[e.tag] = e.text
            content.append(dic)
        return{'status_code': 200, 'CDR': content}


def consultaCliente(cifnif):
    try:
        params = {"fiscalId": cifnif}
        response = makeCall("getCliente", params)
        string = response.read()
        root = ET.fromstring(string)
        content = []
        for a in root[0][0][0]:
            dic = {}
            for e in a:
                dic[e.tag] = e.text
            content.append(dic)
        return {'status_code': response.status, 'clientes': content}
    except Exception as error:
        print(error)
    return None


def altaCliente(linea):
    print('[FUNCTION] --> altaCliente')

    cliente = linea.codcliente
    with open(cliente.cifnif_imageA.path, "rb") as image_file:
        documentFileBase64 = base64.b64encode(image_file.read())
    birthday = None
    if cliente.birthday_omv:
        birthday = cliente.birthday_omv.strftime('%d/%m/%Y')

    params = {
        "subscriberType": cliente.tipo_cliente,
        "marketingConsent": cliente.newsletter,
        "documentType": cliente.tipo_documento,
        "fiscalId": cliente.cifnif,
        "contactName": cliente.nombre,
        "contactFamilyName1": cliente.apellido,
        "emailAddress": cliente.email,
        "contactPhone": cliente.telefono,
        "addressRegion": linea.coddir.idprovincia.codcomunidad.nombre,
        "addressProvince": linea.coddir.idprovincia.provincia,
        "addressCity": linea.coddir.ciudad,
        "addressPostalCode": linea.coddir.codpostal,
        "addressStreet": linea.coddir.direccion,
        "addressNumber": '-', "birthday": birthday,
        "documento_name": cliente.cifnif_imageA.name.split('/')[1],
        "documento": documentFileBase64
    }

    if cliente.tipo_cliente == 1:
        params['fiscalId'] = linea.coddir.cifnif
        params['contactFiscalId'] = cliente.cifnif
        params['contactDocumentType'] = cliente.tipo_documento
        params['documentType'] = 4
        params['name'] = cliente.nombrecomercial
    else:
        params['fiscalId'] = cliente.cifnif
        params['documentType'] = cliente.tipo_documento

    alta = makeCall("setAltaClienteFinal", params)
    if alta.status == 403:
        return {'status_code': 403}
    else:
        try:
            root = ET.fromstring(alta.read())
            response = root[0].find(
                'setAltaClienteFinalResponse').find('return').text
            return {
                'status_code': alta.status, 'response_code': response}
        except Exception:
            return {'status_code': 400}


def altaLinea(linea, icc, dc):

    print('[altaLinea]')

    cliente = linea.codcliente

    if cliente.tipo_cliente == 1:
        print('[tipoCliente]--> 1')
        clientes = consultaCliente(linea.coddir.cifnif)
    else:
        print('[tipoCliente]--> ', cliente.tipo_cliente)
        clientes = consultaCliente(cliente.cifnif)

    print('[clientes]', clientes)

    # if len(clientes['clientes']) == 0:
    if not clientes or len(clientes['clientes']) == 0:
        print('[clienteNoExiste] --> altaCliente')
        alta = altaCliente(linea)
    else:
        print('doss')
        try:
            tipo_cliente = int(clientes['clientes'][0]['suscriberType'])
            if tipo_cliente != cliente.tipo_cliente:
                cliente.tipo_cliente = tipo_cliente
                cliente.save()
        except Exception:
            pass
        alta = {'status_code': 200, 'response_code': '0001'}

    if alta['status_code'] == 200 and alta['response_code'] == '0001':
        print('okeiieieie')
        pool = getpool()
        print('Response getpool --> ', pool)
        movil = pool['numbers']['n1']
        print('MOVIL --> ', movil)

        # REVISAR
        subtarifa_movil = filter(lambda x: (x.tipo_tarifa == 1),
                                 linea.codtarifa.getSubtarifas)
        ###############

        # tarifa = subtarifa_movil[0].subtarifa_siglas_omv
        tarifa = 'MOUNLIMITED'
        params = {
            'tarifa': tarifa,
            'subscriberType': cliente.tipo_cliente,
            'icc': icc,
            'digito_control': dc,
            'telefono': movil,
            'codigo_reserva': pool['numbers']['codigo_reserva'],
            'responseNsolicitud': 'S'
        }

        if cliente.tipo_cliente == 1:
            params['nif'] = linea.coddir.cifnif
        else:
            params['nif'] = cliente.cifnif
        print('FUNCTION --> setAltaLineaNueva')
        print('PARAMS --> ', params)
        alta = makeCall("setAltaLineaNueva", params)
        print('RESPUESTA setAltaLineaNueva --> ', alta)
        print('status --> ', alta.status)

        if alta.status == 403:
            return {'status_code': 403, 'message': 'OMV error inesperado',
                    'response_code': 403}
        else:
            try:
                string = alta.read()
                root = ET.fromstring(string)

                print(root)
                response = root[0].find(
                    'setAltaLineaNuevaResponse').find('return').text
                try:
                    message = errorMessage('altaLinea', response)['message']
                    response_code = response
                except Exception:
                    message = "Linea dada de alta. N. Solicitud: %s" % str(
                        response)
                    response_code = '0001'
                return {'status_code': alta.status, 'message': message,
                        'response_code': response_code, 'movil': movil,
                        'n_solicitud': response[2:-2]}
            except Exception:
                return {'status_code': 400, 'message': 'Error 400',
                        'response_code': 400}
    else:
        return{
            'status_code': alta['status_code'],
            'message': errorMessage(
                'altaCliente', alta['response_code']
            )['message'], 'response_code': alta['response_code']}


def portabilidadLinea(linea, icc, dc):

    cliente = linea.codcliente
    modalidad = 'postpago'
    if linea.tipoTarifaAntigua == 1:
        modalidad = 'prepago'

    if cliente.tipo_cliente == 1:
        clientes = consultaCliente(linea.coddir.cifnif)
    else:
        clientes = consultaCliente(cliente.cifnif)

    if clientes:
        if len(clientes['clientes']) == 0:
            alta = altaCliente(linea)
    else:
        try:
            tipo_cliente = int(clientes['clientes'][0]['suscriberType'])
            if tipo_cliente != cliente.tipo_cliente:
                cliente.tipo_cliente = tipo_cliente
                cliente.save()
        except Exception:
            pass
        alta = {'status_code': 200, 'response_code': '0001'}

    if alta['status_code'] == 200 and alta['response_code'] == '0001':
        # pool = getpool()
        # subtarifa_movil = filter(lambda x: (x.tipo_tarifa == 1),
        #                          linea.codtarifa.getSubtarifas)
        # tarifa = subtarifa_movil[0].subtarifa_siglas_omv

        # DATOS FAKE
        tarifa = 'MOUNLIMITED'
        icc = '893490307130123092'
        dc = '7'
        telefono = '646888873'

        params = {
            'tarifa': tarifa,
            'subscriberType': cliente.tipo_cliente,
            'icc': icc,
            'digito_control': dc,
            # 'telefono': linea.mobil,
            'modalidad_actual': modalidad,
            'telefono': telefono,
            # 'icc_origen': linea.icc_anterior,
            # 'dc_origen': linea.dc_icc_anterior,
            'icc_origen': icc,
            'dc_origen': dc,
            'responseNsolicitud': 'S'
        }

        if cliente.tipo_cliente == 1:
            params['nif'] = linea.coddir.cifnif
        else:
            params['nif'] = cliente.cifnif

        portabilidad = makeCall("setAltaLineaPortabilidad", params)
        if portabilidad.status == 403:
            return {
                'status_code': 403, 'message': 'OMV error inesperado',
                'response_code': 403
            }
        else:
            try:

                root = ET.fromstring(portabilidad.read())

                # Esto no tiene ningun sentido... da bucle infinito llamandose a si misma
                # constantemente :S:S:S:S

                response = root[0].find(
                    'setAltaLineaPortabilidadResponse').find('return').text

                print('[RESPONSE] setAltaLineaPortabilidadResponse => ')
                print(response)
                print('-------------------------------------------')

                try:
                    message = errorMessage(
                        'portabilidadLinea', response)['message']
                    response_code = response
                except Exception as error:
                    print('[ERROR MESSAGE]')
                    print(error)
                    message = response
                    response_code = '0001'

                respuesta = {
                    'status_code': portabilidad.status,
                    'message': message,
                    'response_code': response_code,
                    'movil': linea.mobil,
                    'n_solicitud': response[2:-2]
                }
                print('[RESPUESTA] => ')
                print respuesta
                print('-----------------')

                return {'status_code': 400, 'message': 'Error 400',
                        'response_code': 400}

                return respuesta
            except Exception as error:
                print(['ERROR'])
                print (error)
                return {'status_code': 400, 'message': 'Error 400',
                        'response_code': 400}
    else:
        return{
            'status_code': alta['status_code'],
            'message': errorMessage(
                'altaCliente', alta['response_code']
            )['message'], 'response_code': alta['response_code']}


def enviarDocumento(linea):

    if linea.signature_id and linea.document_id:
        signaturit = SignaturitClient(settings.SIGNATURIT_ACCESS_TOKEN)
        document = signaturit.download_signed_document(
            linea.signature_id,
            linea.document_id)
        documentFileBase64 = base64.b64encode(document)

        cliente = linea.codcliente
        params = {
            "subscriberType": cliente.tipo_cliente,
            "codigo_solicitud": linea.omv_solicitud,
            "documento_name": "%s_%s.pdf" % (cliente.pk, linea.pk),
            "documento": documentFileBase64
        }

        if linea.origen == 0:
            params['tipo_documento'] = 'CONTRATO'
        else:
            params['tipo_documento'] = 'PORTABILIDAD'

        if cliente.tipo_cliente == 1:
            params['nif_cliente'] = linea.coddir.cifnif
        else:
            params['nif_cliente'] = cliente.cifnif

        subida = makeCall("subirDocumento", params)
        if subida.status == 403:
            return {'status_code': 403, "message": "Bad request"}
        else:
            try:
                string = subida.read()
                root = ET.fromstring(string)
                response = root[0].find(
                    'subirDocumentoResponse').find('return').text
                try:
                    message = errorMessage(
                        'subirDocumento', response)['message']
                    response_code = response
                except Exception:
                    message = response
                    response_code = '0001'
                return {'status_code': subida.status, 'message': message,
                        'response_code': response_code}
                return {
                    'status_code': subida.status, 'response_code': response}
            except Exception as msg:
                return {'status_code': 400, "message": msg}
    else:
        return {'status_code': 400, "message": "document not signed"}


def cancelarSolicitud(omv_solicitud):

    params = {"codigo": str(omv_solicitud)}
    subida = makeCall("cancelLineasSolicitud", params)
    if subida.status == 403:
        return {'status_code': 403}
    else:
        try:
            string = subida.read()
            root = ET.fromstring(string)
            response = root[0].find(
                'cancelLineasSolicitudResponse').find('return').text
            try:
                message = errorMessage(
                    'cancelLineasSolicitud', response)['message']
                response_code = response
                return {'status_code': subida.status, 'message': message,
                        'response_code': response_code}
            except Exception:
                return {'status_code': 400,
                        'message': 'Error insperado OMV'}

        except Exception:
            return {'status_code': 400,
                    'message': 'Error insperado OMV'}


def activarBuzonDeVoz(linea):

    datos = {}
    # datos['user'] = 'XXXXXXXXX'
    # datos['pass'] = 'XXXXXXXXX'
    datos['telefono'] = linea.mobil
    datos['servicios'] = {}
    datos['servicios']['CfnrcActive'] = True
    datos['servicios']['CfnrcextString'] = '123'

    return (makeCall("setServicios", datos))

    # Call OMV function
    # user
    # pass
    # telefono
    # servicios []
    #   CfnrcActive     True
    #   CfnrcextString  600323449

    # $client->call("setServicios",array($datos));


def desactivarBuzonDeVoz(linea):
    # Model MobilsClients
    datos = {}
    # datos['user'] = 'XXXXXXXXX'
    # datos['pass'] = 'XXXXXXXXX'
    datos['telefono'] = linea.mobil
    datos['servicios'] = {}
    datos['servicios']['CfnrcActive'] = False

    return (makeCall("setServicios", datos))

    # Call OMV function
    # user
    # pass
    # telefono
    # servicios []
    #   CfnrcActive     False
    #$client->call("setServicios",array($datos));


def activarRoaming(linea):

    datos = {}
    # datos['user'] = 'XXXXXXXXX'
    # datos['pass'] = 'XXXXXXXXX'
    datos['telefono'] = linea.mobil
    datos['servicios'] = {}
    datos['servicios']['Boic'] = True

    return (makeCall("setServicios", datos))

    # Call OMV function
    # user
    # pass
    # telefono
    # servicios []
    #   Boic     True


def desactivarRoaming(linea):

    datos = {}
    # datos['user'] = 'XXXXXXXXX'
    # datos['pass'] = 'XXXXXXXXX'
    datos['telefono'] = linea.mobil
    datos['servicios'] = {}
    datos['servicios']['Boic'] = False

    return (makeCall("setServicios", datos))

    # Call OMV function
    # user
    # pass
    # telefono
    # servicios []
    #   Boic     False
