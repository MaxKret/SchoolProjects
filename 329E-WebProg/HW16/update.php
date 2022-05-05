<!DOCTYPE html>
<html lang="en">

<head>
	<title>Update</title>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="description" content="SQL">
	<meta name="author" content="Maxwell Kretschmer">
	<link rel="stylesheet" href="login.css">
</head>

<body>
	<h1 id="titleText"> SQL </h1>
	<div class="centering-flex-container">
		<div class="centering-flex-container">
			<div class="main">
				<h2> Update </h2>
				<div class="centering-container">
					<div class="logregContainer">
						<form method="POST">
						<p>
								<label>ID:</label>
								<input name="u_id" id="u_id" type="text" required/>
							</p>
							<p>
								<label>Last Name:</label>
								<input name="u_last" id="u_last" type="text"/>
							</p>
							<p>
								<label>First Name:</label>
								<input name="u_first" id="u_first" type="text"/>
							</p>
							<p>
								<label>Major:</label>
								<input name="u_major" id="u_major" type="text"/>
							</p>
							<p>
								<label>GPA:</label>
								<input name="u_gpa" id="u_gpa" type="text"/>
							</p>
							<p>
								<button type="submit" name="submitQ" id="submitQ">Submit</button>
								<input type="reset" value="Clear" />
							</p>
						</form>
					</div>
				</div>
				<br>
				<div class="centering-container">
					<div class="logregContainer">
						<span>
							OUTPUT <br>
						</span>
						<span>
<?php
// CONNECT TO DB
$server = "spring-2022.cs.utexas.edu";
$dbName = "cs329e_bulko_maxkret";
$user = "cs329e_bulko_maxkret";
$pwd = "warsaw7mortar&canvas";
$mysqli = new mysqli($server, $user, $pwd, $dbName);
if ($mysqli->connect_errno) {
	echo "failure";
	die('Connect Error: ' . $mysqli->connect_errno . ": " . $mysqli->connect_error);
}

// VARS AND FUNCS
$g_id = $_POST['u_id'];
$g_id = ($g_id === "") ? NULL : $g_id;
$g_last = $_POST['u_last'];
$g_last = ($g_last === "") ? NULL : $g_last;
$g_first = $_POST['u_first'];
$g_first = ($g_first === "") ? NULL : $g_first;
$g_major = $_POST['u_major'];
$g_major = ($g_major === "") ? NULL : $g_major;
$g_gpa = $_POST['u_gpa'];
$g_gpa = ($g_gpa === "") ? NULL : $g_gpa;


function get_querytext($varset, $g_ID, $g_LAST = NULL, $g_FIRST = NULL, $g_MAJOR = NULL, $g_GPA = NULL)
{
	$qStart = "UPDATE STUDENTS " .
		"SET ";
	$qEnd = " WHERE ID = \"$g_ID\";";
	$qTextArr = array();
	for ($i = 0; $i < 4; $i++) {
		switch ($i) {
			case 0:
				if ($varset[$i] === 'true') {
					$qTextArr[] = "LASTNAME = \"$g_LAST\"";
				}
				break;
			case 1:
				if ($varset[$i] === 'true') {
					$qTextArr[] = "FIRSTNAME = \"$g_FIRST\"";
				}
				break;
			case 2:
				if ($varset[$i] === 'true') {
					$qTextArr[] = "MAJOR = \"$g_MAJOR\"";
				}
				break;
			case 3:
				if ($varset[$i] === 'true') {
					$qTextArr[] = "GPA = \"$g_GPA\"";
				}
				break;
		}
	}
	return $qStart . implode(", ", $qTextArr) . $qEnd;
}
$varset_arr = array(
	isset($g_last) ? 'true' : 'false',
	isset($g_first) ? 'true' : 'false',
	isset($g_major) ? 'true' : 'false',
	isset($g_gpa) ? 'true' : 'false',
);
if ($varset_arr === ["false", "false", "false", "false"]) {
// exit();
}
else {
	// GET RECORD
	$query_text = get_querytext($varset_arr, $g_id, $g_last, $g_first, $g_major, $g_gpa);
	if ($query_text) {
		$query = $mysqli->query($query_text);
	}

	if (!$query) {
		echo "Error";
		die("Query failed: ($mysqli->error <br> SQL command = $query");
	}
	else {
		echo "Success";
	}
}
?>
						</span>
					</div>
				</div>
			</div>
		</div>
	</div>
</body>
</html>