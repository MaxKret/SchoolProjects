<?php
	session_start();
	$op = $_REQUEST["op"];
	$key = $_REQUEST["key"];
	$val = $_REQUEST["val"];
	
	// SET
	if ($op === "set") {
		// REDIRECT
		if($key === "redirect") {
			$_SESSION["redirect_url"] = $val;
		}
		// ACCOUNT
		elseif($key === "loggedin") {
			$_SESSION["loggedin"] = $val;
		}
		// COOKIE
		elseif($key === "cookie") {
			setcookie("accountCookie", $val, time() + 120);
		}
	}

	//  GET
	elseif ($op === "get") {
		// REDIRECT
		if($key === "redirect") {
			$ret = $_SESSION["redirect_url"];
			echo $ret;
		}
		// ACCOUNT
		elseif($key === "loggedin") {
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