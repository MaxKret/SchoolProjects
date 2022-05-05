<!DOCTYPE html>
<html lang="en">

<head>
	<title>Insert</title>
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
				<h2> Insert </h2>
				<div class="centering-container">
					<div class="logregContainer">
						<form method="POST">
							<p>
								<label>ID:</label>
								<input name="i_id" id="i_id" type="text" required/>
							</p>
							<p>
								<label>Last Name:</label>
								<input name="i_last" id="i_last" type="text" required/>
							</p>
							<p>
								<label>First Name:</label>
								<input name="i_first" id="i_first" type="text" required/>
							</p>
							<p>
								<label>Major:</label>
								<input name="i_major" id="i_major" type="text" required/>
							</p>
							<p>
								<label>GPA:</label>
								<input name="i_gpa" id="i_gpa" type="text" required/>
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
$g_id = $_POST['i_id'];
$g_last = $_POST['i_last'];
$g_first = $_POST['i_first'];
$g_major = $_POST['i_major'];
$g_gpa = $_POST['i_gpa'];


if (!isset($g_id)){}
else {
	// GET RECORD
	$query_text = "INSERT INTO STUDENTS VALUES " .
				"(\"$g_id\",\"$g_last\",\"$g_first\",\"$g_major\",\"$g_gpa\");";
	$query = $mysqli->query($query_text);

	if (!$query) {
		echo "Error";
		die("Query failed: ($mysqli->error <br> SQL command = $query");
	}
	else{
		echo "Success!";
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