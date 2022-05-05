<?php
	$prevuser = $_REQUEST["prevuser"];
	$is_new = "";

	if ($fh = fopen("prev_users.txt", "r")) {
		$whole_file = fread($fh, filesize("prev_users.txt"));
		if (substr_count($whole_file, $prevuser) >= 1) {
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