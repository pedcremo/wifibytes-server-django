import string
import os
import sys
import httplib
from lxml import objectify, etree

import xml.etree.ElementTree as ET

import urllib2


def getLineas():
    server_addr = "optel.airenetworks.es:6547"
    service_action = "/ws_desarrollo/mv/gestMOVIL_2.php?WSDL"

    body = """<soapenv:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:tns="URN:IONMOBILEWS" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns="http://schemas.xmlsoap.org/wsdl/" targetNamespace="URN:IONMOBILEWS">
	<soapenv:Header/>
	<soapenv:Body>
	<ns:getLineas>
	<ns:userinfo>
	<ns:user>%s</ns:user>
	<ns:pass>%s</ns:pass>
	</ns:userinfo>
	</ns:getLineas>
	</soapenv:Body>
	</soapenv:Envelope>""" % ("B-98137078", "xGhbuwzPeD")

    request = httplib.HTTPConnection(server_addr)
    request.putrequest("POST", service_action)
    request.putheader("Accept", "application/soap+xml, application/dime, multipart/related, text/*")
    request.putheader("Content-Type", "text/xml; charset=utf-8")
    request.putheader("Cache-Control", "no-cache")
    request.putheader("Pragma", "no-cache")
    request.putheader("SOAPAction", "http://" + server_addr + service_action)
    request.putheader("Content-Length", str(len(body)))
    request.endheaders()
    request.send(body)
    response = request.getresponse().read()

    print response

    root = ET.fromstring(response)
    content = []

    for a in root.iter():
        print a

    '''
	for a in root[0][0][0]:  # iter root
	    print "-"*30
	    for e in a:
	    	print e.tag,":",e.text
	'''


getLineas()
