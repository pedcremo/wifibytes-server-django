import urllib
import urllib2


# omv url  api conexion

def test_conection():
    url = 'https://developer.temasys.com.sg/rest/login/'
    values = {
        "username": "dbarenas",
        "password": "my123098"}

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()

    print the_page

    url = 'https://developer.temasys.com.sg/rest/usages/'
    values = {
        "apiKey": "e88ee375-2b97-4438-92ed-b8e8943869c0"}

    data = urllib.urlencode(values)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()

    return the_page

#
# CONSULTA POOL NÚMEROS LIBRES
#
#<?
# require_once "nusoap.php";
#  $client = new nusoap_client($wsdl,true, $proxyhost=false, $proxyport=false, $proxyusername=false,
# $proxypassword=false, $timeout=0, $response_timeout=160);

#  $err = $client->getError();
#  if ($err)
#  {
#  // Display the error
#  echo "<h2>Constructor error</h2><pre>".$err."</pre>";
#  // At this point, you know the call that follows will fail
#  }
#  $datos=array();
#  $datos["user"]="";
#  $datos["pass"]="";
#  $result = $client->call("getPoolMsisdn",array($datos));
#  print_r($datos);?>


# def getPoolMsisdn(conexion):
#     arrayNumbers =  # $result = $client->call("getPoolMsisdn",array($datos));
#     return arrayNumbers


#
# CONSULTA DE CDR  consumos de user por mes para factura de mes y datos para grafico historico de consumo
#
# <?
# require_once "nusoap.php";
# $wsdl = "http://optel.airenetworks.es:6547/ws/mv/gestMOVIL.php?wsdl";
# $cliente = new nusoap_client($wsdl, true);
# $datos = array("user" => " ", "pass" => " ", "mes" => " ", “anyo” => “ “, “tipo_servicio” => “ “);
# $result = $client->call("getCDR", array($datos));
# $error = $client->getError();
# if ($error)
# echo "<pre>".$error."</pre>";
# print_r($result);
# ?>
#
# def getDataFactura(conexion):



#
# CONSULTAR los servicios en linea
#
# <?
# require_once "nusoap.php";
#  $client = new nusoap_client($wsdl,true, $proxyhost=false, $proxyport=false, $proxyusername=false,
# $proxypassword=false, $timeout=0, $response_timeout=160);

#  $err = $client->getError();
#  if ($err)
#  {
#  // Display the error
#  echo "<h2>Constructor error</h2><pre>".$err."</pre>";
#  // At this point, you know the call that follows will fail
#  }
#  $datos=array();
#  $datos["user"]="";
#  $datos["pass"]="";
# $datos["telefono"]="";
#  $result = $client->call("getServicios",array($datos));
#  print_r($datos);?>



#
# MODIFICAR LOS SERVICIOS DE UNA LÍNEA
#
# <?
# require_once "nusoap.php";
#  $client = new nusoap_client($wsdl,true, $proxyhost=false, $proxyport=false, $proxyusername=false,
# $proxypassword=false, $timeout=0, $response_timeout=160);

#  $err = $client->getError();
#  if ($err)
#  {
#  // Display the error
#  echo "<h2>Constructor error</h2><pre>".$err."</pre>";
#  // At this point, you know the call that follows will fail
#  }
#  $datos=array();
#  $datos["user"]="";
#  $datos["pass"]="";
# $datos["telefono"]="";
# $servicios=array();
# $servicios["BoicActive"]="true";//Activar el bloqueo para llamadas internacionales
# $datos['servicios']=$servicios;
#  $result = $client->call("setServicios",array($datos));
#  print_r($datos);?>
#----
# Array [servicios] – Ejemplo para Desactivar Buzón y enviar SMS cuando el terminal este apagado
# Campo Tipo Obligatorio Valores
# CfnrcActive String Si true
# CfnrcextString String Si 34602209999
# Array [servicios] – Ejemplo para Activar Buzón cuando el usuario no contesta en 15 segundos
# Campo Tipo Obligatorio Valores
# CfnryActive String Si true
# CfnryExtNumber Int Si 15
# CfnryextString String Si 121
#
# def modificarServicios(conexion):


#
# SET ALTA LINEA NUEVA
#
# <?
# require_once "nusoap.php";
# $wsdl = "http://optel.airenetworks.es:6547/ws/mv/gestMOVIL.php?wsdl";

# $cliente = new nusoap_client($wsdl, true);
# $datos = array("user" => " ", "pass" => " ", “tarifa” => “ “, “nif” => “ “, “icc” => “ “, “digito_control” => “ “,
# “teléfono” => “ “);
# $result = $client->call("setAltaLineaNueva", array($datos));
# $error = $client->getError();
# if ($error)
# echo "<pre>".$error."</pre>";
# print_r($result);
# ?>
def setAltaLineaNueva(conexion):





#
#ALTA DE PORTAVILIDAD
#
# <?
# require_once "nusoap.php";
# $wsdl = "http://optel.airenetworks.es:6547/ws/mv/gestMOVIL.php?wsdl";

# $cliente = new nusoap_client($wsdl, true);
# $datos = array("user" => " ", "pass" => " ", “tarifa” => “ “, “nif” => “ “, “icc” => “ “, “digito_control” => “ “,
# “teléfono” => “ “, “modalidad_actual” => “ “, “icc_origen” => “ “, “dc_origen” => “ “);
# $result = $client->call("setAltaLineaPortabilidad", array($datos));
# $error = $client->getError();
# if ($error)
# echo "<pre>".$error."</pre>";
# print_
def setAltaLineaPortabilidad():


#  Parámetros de entrada.
# En la siguiente tabla se muestran los parámetros de entrada del servicio.
# CAMPO TIPO Obligatorio Descripción / Ejemplo
# user String Si Usuario de acceso a la oficina virtual, EJ: B65498765.
# pass String Si Contraseña de acceso a la oficina virtual.
# suscriberType Int Si Tipo de Cliente final.
# nif_cliente String Si NIF del titular de la línea.
# codigo_solicitud String Si Código de la solicitud de línea para subir el documento.
# documento File Si Documento de la línea. Se deberá de enviar el
# contenido del fichero codificado en base 64
# tipo_documento String Si Tipo de documento del cliente final. DOCUMENTO /
# PORTABILIDAD / CONTRATO 

# //Fichero
# $tmpfile = $_FILES[“fichero”][“tmp_name”]; //temp filename
# $filename_documento = $_FILES[“fichero”][“name”]; //Original filename
# If(strlen($filename_documento) > 0)
# {
# $handle = fopen($tmpfile, “r”); //Open the themp file
# $contents = fread($handle, filesize($tmpfile)); //Read the temp file
# fclose($handle); //Close the temp file
# $decodeContent_fact = base64_encode($contents);
# //Decode the filecontent, so that we code send a binary string to SOAP
# }
# $datos[“documento”] = $decodeContent_fact;
# $datos[“documento_name”] = str_replace(‘ ‘,’’,$filename_fact);
# $result = $client->call("subirDocumento", array($datos));
# $error = $client->getError();
def subida documentosTipo()




# falta # 1. ALTA DE CLIENTES FINALES
#falta # 2. CONSULTA DE CLIENTES FINALES
#falta # 3. MODIFICACIÓN DE CLIENTES FINALES
# 4. CONSULTA DE CDR
#falta # 5. CONSULTA DE TARIFAS
#falta # 6. CONSULTA DE LÍNEAS
#falta # 7. ESTABLECER ALERTA DE FACTURACIÓN
#falta # 8. OBTENER SOLICITUDES DE LÍNEAS
# 9. ALTA DE LÍNEAS NUEVAS
# 10. ALTA DE PORTABILIDADES
# falta# 11. CAMBIOS DE TITULAR
# 12. SUBIDA DE DOCUMENTOS
#falta # 13. OBTENER DOCUMENTOS
#falta # 14. SOLICITAR CORTE POR IMPAGO
# falta# 15. CANCELAR SOLICITUD CORTE IMPAGO
# falta# 16. REESTABLECER CORTE POR IMPAGO
# 17. CONSULTA POOL NUMEROS LIBRES
# 18. CONSULTA SERVICIOS DE LA LINEA
# 19. MODIFICAR SERVICIOS DE LA LÍNEA
