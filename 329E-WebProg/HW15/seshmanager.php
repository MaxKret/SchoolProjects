<?php
	session_start();
	$op = $_REQUEST["op"];
	if ($op === "set") {
		$user = $_REQUEST["loginUser"];
		$_SESSION['loggedin'] = $user;
	}
	elseif ($op === "clear") {
		$_SESSION['loggedin'] = "false";
		session_destroy();
	}
?>