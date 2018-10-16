import zeep
import json


wsdl = 'http://optel.airenetworks.es:6547/ws_desarrollo/mv/gestMOVIL_2.php?WSDL'
client = zeep.Client(wsdl=wsdl, strict=False)

datos = {
    "user": "B-98137078",
    "pass": "xGhbuwzPeD"
}
#resp = client.service.getTarifas(datos)

print (resp)
input_dict = helpers.serialize_object(resp)
output_dict = json.loads(json.dumps(input_dict))

print (output_dict)


python - mzeep http: // optel.airenetworks.es: 6547 / ws_desarrollo / mv / gestMOVIL_2.php


python - mzeep http: // www.soapclient.com / xml / soapresponder.wsdl


$content=$(curl -L http://optel.airenetworks.es:6547/ws_desarrollo/mv/gestMOVIL_2.php?WSDL)
echo $content

content =$(curl -L http://www.webservicex.net/globalweather.asmx?WSDL)
echo $content


$ curl http://www.webservicex.net/globalweather.asmx?WSDL  | xmllint --format -
$ curl https://api.twitter.com/1/help/configuration.json | python -mjson.tool


content=$(curl -L http://www.webservicex.net/globalweather.asmx?WSDL)
echo $content


content=$(curl -L http://optel.airenetworks.es:6547/ws_desarrollo/mv/gestMOVIL_2.php?WSDL)
echo $content
