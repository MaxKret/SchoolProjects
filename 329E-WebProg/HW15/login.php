<?php
session_start();
$user = $_REQUEST["loginUser"];
$password = $_REQUEST["loginPass"];
$entry = $user . ":" . $password;
$is_new = "";

if ($fh = fopen("passwd.txt", "r")) {
	$whole_file = fread($fh, filesize("passwd.txt"));
	if (substr_count($whole_file, $entry) >= 1) {
		fclose($fh);
		$is_new = "false";
	}
	else{
		fclose($fh);
		$is_new = "true";
		if ($fw = fopen("passwd.txt", "a")) {
			fwrite($fw, "$entry \n");
			fclose($fw);
		}
	}
	echo $is_new;
}
else {
	echo "error: no file found";
}
?>