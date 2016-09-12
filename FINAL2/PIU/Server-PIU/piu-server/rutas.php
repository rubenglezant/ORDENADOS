<?php

// Parada es el parametro para retornar debe ir en la consulta

// Este es un ejemplo
if($_GET["parada"] === "23") {

	// Conectandose
	$enlace =  mysql_connect('localhost', 'root', 'root');
	if (!$enlace) {
	    die('No pudo conectarse: ' . mysql_error());
	}
	mysql_select_db("piu", $enlace);

	// Ejecutar la consulta
	$resultado = mysql_query("select * from horas order by minutos");

	// Comprobar el resultado
	// Lo siguiente muestra la consulta real enviada a MySQL, y el error ocurrido. Útil para depuración.
	if (!$resultado) {
	    $mensaje  = 'Consulta no válida: ' . mysql_error() . "\n";
	    $mensaje .= 'Consulta completa: ' . $consulta;
	    die($mensaje);
	}	

	// Usar el resultado
	// Si se intenta imprimir $resultado no será posible acceder a la información del recurso
	// Se debe usar una de las funciones de resultados de mysql
	// Consulte también mysql_result(), mysql_fetch_array(), mysql_fetch_row(), etc.
	$dataTotal = array();
	while ($fila = mysql_fetch_assoc($resultado)) {
	    $data1 = array( $fila['buslinea'], $fila['minutos']);
	    // $dataTotal.append($data1);	
	    array_push($dataTotal, $data1);
	}
	header('Content-type: application/json');
  	echo json_encode( $dataTotal );
}

?>
