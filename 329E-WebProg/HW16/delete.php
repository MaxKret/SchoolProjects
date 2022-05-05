<!DOCTYPE html>
<html lang="en">

<head>
	<title>Delete</title>
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
				<h2> Delete </h2>
				<div class="centering-container">
					<div class="logregContainer">
						<form method="POST">
							<p>
								<label>ID:</label>
								<input name="d_id" id="d_id" type="text" required/>
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
$g_id = $_POST['d_id'];

if (!isset($g_id)){}
else {
	// GET RECORD
	$query_text = "DELETE FROM STUDENTS " .
				"WHERE ID = \"$g_id\";";
	$query = $mysqli->query($query_text);

	if (!$query) {
		echo "Error";
		die("Query failed: ($mysqli->error <br> SQL command = $query");
	}
	else{
		echo "Deleted or doesn't exist";
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