<?
require_once "nusoap/lib/nusoap.php";
$wsdl = "http://optel.airenetworks.es:6547/ws_desarrollo/mv/gestMOVIL_2.php?wsdl";

$cliente = new nusoap_client($wsdl, true);
$datos = array("user" => "B98137078", "pass" => "xGhbuwzPeD");
$result = $client->call("getTarifas", array($datos));
$error = $client->getError();
if ($error)
echo "<pre>".$error."</pre>";
print_r($result);
?>


<?php
require_once "nusoap/lib/nusoap.php";
$wsdl = "http://optel.airenetworks.es:6547/ws_desarrollo/mv/gestMOVIL_2.php?wsdl";
$client = new nusoap_client($wsdl,true, $proxyhost=false, $proxyport=false, $proxyusername=false, $proxypassword=false, $timeout=0, $response_timeou$
$err = $client->getError(); if ($err)
{
// Display the error
echo "<h2>Constructor error</h2><pre>".$err."</pre>"; // At this point, you know the call that follows will fail
}
$datos=array();
$datos["user"]="B98137078";
$datos["pass"]="xGhbuwzPeD";
$result = $client->call("getTarifas",array($datos));
print_r($
?>


<?php
require_once "nusoap/lib/nusoap.php";
$wsdl = "http://optel.airenetworks.es:6547/ws_desarrollo/mv/gestMOVIL_2.php?wsdl";
$client = new nusoap_client($wsdl,true);
$err = $client->getError(); if ($err)
{
// Display the error
echo "<h2>Constructor error</h2><pre>".$err."</pre>"; // At this point, you know the call that follows will fail
}
$datos=array();
$datos["user"]="B98137078";
$datos["pass"]="xGhbuwzPeD";
$result = $client->call("getTarifas",array($datos));
print_r($result);
?>
