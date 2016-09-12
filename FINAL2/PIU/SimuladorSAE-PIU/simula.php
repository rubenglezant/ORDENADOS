<?php
// Conectandose
$enlace =  mysql_connect('localhost', 'root', 'root');
if (!$enlace) {
    die('No pudo conectarse: ' . mysql_error());
}
echo 'Conectado satisfactoriamente';
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
while ($fila = mysql_fetch_assoc($resultado)) {
    $min = $fila['minutos'] - 1;
    if ($min < 0)
	$min = 22;
    $update="UPDATE horas SET minutos=".$min." WHERE buslinea='".$fila['buslinea']."'";
    mysql_query($update);
}

// Liberar los recursos asociados con el conjunto de resultados
// Esto se ejecutado automáticamente al finalizar el script.
mysql_free_result($resultado);
mysql_close($enlace);
?>

