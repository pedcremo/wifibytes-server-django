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
$datos["telefono"]="652416660";

$result = $client->call("getServicios",array($datos));
print_r($result);
?>
