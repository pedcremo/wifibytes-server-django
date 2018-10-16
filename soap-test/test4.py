import logging
from suds.client import Client
from datetime import datetime
from suds.plugin import MessagePlugin


class Filter(MessagePlugin):
    def received(self, context):
        reply = context.reply
        context.reply = reply[reply.find("<s:Envelope"):reply.rfind(">") + 1]


logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)

client = Client(
    'http://optel.airenetworks.es:6547/ws_desarrollo/mv/gestMOVIL_2.php?wsdl', plugins=[Filter()])
request = client.factory.create('ns1:getTarifasRequest')
request.datos = {
    "user": "B-98137078",
    "pass": "xGhbuwzPeD"
}
result = client.service['basic'].getTarifas(request)
