from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor
url = 'http://optel.airenetworks.es:6547/ws_desarrollo/mv/gestMOVIL_2.php?wsdl'
imp = Import('http://www.w3.org/2001/XMLSchema')
doctor = ImportDoctor(imp)
client = Client(url, doctor=doctor)
print (client)
