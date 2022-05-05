<?php
	session_start();
	$op = $_REQUEST["op"];
	$key = $_REQUEST["key"];
	$val = $_REQUEST["val"];
	
	// SET
	if ($op === "set") {
		// ACCOUNT
		if($key === "loggedin") {
			$_SESSION["loggedin"] = $val;
		}
		// COOKIE
		elseif($key === "cookie") {
			setcookie("accountCookie", $val, time() + 3600);
		}
	}

	//  GET
	elseif ($op === "get") {
		// ACCOUNT
		if($key === "loggedin") {
			$ret = $_SESSION["loggedin"];
			echo $ret;
		}
		// COOKIE
		elseif($key === "cookie") {
			$ret = $_COOKIE["accountCookie"];
			if (isset($ret)) {
				echo $ret;
			}
			else {
				echo "false";
			}
		}
	}
	
	else { echo "no op";}
?>