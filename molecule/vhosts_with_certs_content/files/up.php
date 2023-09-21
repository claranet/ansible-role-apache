<?php

$status = 'OK';

if ($status == 'OK') {
	header("HTTP/1.1 200 OK");
} else {
	header("HTTP/1.1 503 Unavailable");
}
echo $status;

?>

