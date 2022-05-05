<?php
session_start();
$user = $_REQUEST["loginUser"];
$password = $_REQUEST["loginPass"];
$entry = $user . ":" . $password;
$is_account = "";

if ($fh = fopen("passwd.txt", "r")) {
	$whole_file = fread($fh, filesize("passwd.txt"));
	if (substr_count($whole_file, $entry) >= 1) {
		fclose($fh);
		$is_account = "true";
	}
	else{
		fclose($fh);
		$is_account = "false";
	}
	echo $is_account;
}
else {
	echo "error: no file found";
}
?>