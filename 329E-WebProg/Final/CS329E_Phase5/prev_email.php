<?php
	$email = $_REQUEST["email"];
	$is_new = "";

	if ($fh = fopen("emails.txt", "r")) {
		$whole_file = fread($fh, filesize("emails.txt"));
		if (substr_count($whole_file, $email) >= 1) {
			fclose($fh);
			$is_new = "false";
		}
		else{
			fclose($fh);
			$is_new = "true";
		}
		echo $is_new;
	}
	else {
		echo "error: no file found";
	}
?>