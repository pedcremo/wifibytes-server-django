from suds import WebFault
from suds.client import Client
import traceback as tb
import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
try:
    client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')
    print client.service.ConvertSpeed(100, 'kilometersPerhour', 'milesPerhour')
except WebFault, f:
    print f
    print f.fault
except Exception, e:
    print e
    tb.print_exc()


##########################################################################


from suds import WebFault
from suds.client import Client
from suds.plugin import MessagePlugin
import traceback as tb
import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)


class UnicodeFilter(MessagePlugin):
    def received(self, context):
        decoded = context.reply.decode('utf-8', errors='ignore')
        reencoded = decoded.encode('utf-8')
        context.reply = reencoded


badXML = "definitions.xml"  # (type <str>)
# Turn it into a python unicode string - ignore errors, kick out bad unicode
decoded = badXML.decode('utf-8', errors='ignore')  # (type <unicode>)
# turn it back into a string, using utf-8 encoding.
goodXML = decoded.encode('utf-8')  # (type <str>)

try:
    client = Client(
        'definitions.xml', plugins=[UnicodeFilter()])
    datos = {
        "user": "B-98137078",
        "pass": "xGhbuwzPeD"
    }
    print client.service.getTarifas(datos)
except WebFault, f:
    print f
    print f.fault
except Exception, e:
    print e
    tb.print_exc()


from suds import WebFault
from suds.client import Client
import traceback as tb
import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
try:
    client = Client('http://optel.airenetworks.es:6547/ws_desarrollo/mv/gestMOVIL_2.php?wsdl')
except WebFault, f:
    print f
    print f.fault
except Exception, e:
    print e
    tb.print_exc()
