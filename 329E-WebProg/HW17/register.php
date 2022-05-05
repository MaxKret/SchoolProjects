<?php
// VARS
$s_user = $_POST["user"];
$s_pass = $_POST["pass"];
$db_user = "";
$db_pass = "";

$last_user = "";
$last_pass = "";

// CONNECT TO DB
$server = "spring-2022.cs.utexas.edu";
$dbName = "cs329e_bulko_maxkret";
$user = "cs329e_bulko_maxkret";
$pwd = "warsaw7mortar&canvas";
$mysqli = new mysqli($server, $user, $pwd, $dbName);
if ($mysqli->connect_errno) {
	echo "Error: connection failed";
	die('Connect Error: ' . $mysqli->connect_errno . ": " . $mysqli->connect_error);
}

$queryText = "SELECT * FROM passwords WHERE USER = \"$s_user\";";
$query = $mysqli->query($queryText);

if (!$query) {
	echo "Error: query failed";
	die("Query failed: ($mysqli->error <br> SQL command = $query");
}
else {
	$_match = false;

	while ($record = $query->fetch_row()) {
		$_match = true;
		$db_user = $record[0];
		$db_pass = $record[1];

		if ($db_user !== $last_user) {
			$last_user = $db_user . "";
		}
		if ($db_pass !== $last_pass) {
			$last_pass = $db_pass . "";
		}

	}

	if ($_match) {
		// >= 1 MATCH	
		if (($db_user === $s_user) && ($db_pass === $s_pass)) {
			// PASSWORDS MATCH
			echo "confirm";
		}
		else {
			// PASSWORDS DONT MATCH
			$query_text = "UPDATE passwords SET PASS = \"$s_pass\" WHERE USER = \"$s_user\";";
			$query = $mysqli->query($query_text);

			if (!$query) {
				echo "Error: update failed";
				die("Query failed: ($mysqli->error <br> SQL command = $query");
			}
			else {
				echo "update";
			}
		}


		echo $table;
	}
	else {
		// NO MATCHES: REGISTER
		$query_text = "INSERT INTO passwords (USER,PASS) VALUES (\"$s_user\",\"$s_pass\");";
		$query = $mysqli->query($query_text);

		if (!$query) {
			echo "Error: register failed";
			die("Query failed: ($mysqli->error <br> SQL command = $query");
		}
		else {
			echo "register";
		}
	}
}
?>