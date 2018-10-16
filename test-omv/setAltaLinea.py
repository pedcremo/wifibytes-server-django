    CALL[OMV] - - >
('   [function]-->', 'setAltaLineaNueva')
('   [params]-->', {'icc': 893490307130123190, 'responseNsolicitud': 'S', 'nif': u'48604382T', 'digito_control': 9,
                    'subscriberType': 0, 'codigo_reserva': '1502440138', 'tarifa': 'MOUNLIMITED', 'telefono': '744482598'})
('   [response]-->', < httplib.HTTPResponse instance at 0x7f12cc5d03f8 > )
----------------------------

import string
import os
import sys
import httplib

import xml.etree.ElementTree as ET
import urllib2

server_addr = settings.OMV_SERVER_ADDR
user = settings.OMV_USER
password = settings.OMV_PASSWORD

print ('user', user)
print ('password', password)


arams = {
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
