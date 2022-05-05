<!DOCTYPE html>
<html lang="en">

<head>
	<title>Actions</title>
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
				<h2 style="text-align: center"> Actions </h2>
				<div class="centering-container">
					<span style="text-align: center">
<?php
// CONNECT TO DB
$server = "spring-2022.cs.utexas.edu";
$dbName = "cs329e_bulko_maxkret";
$user = "cs329e_bulko_maxkret";
$pwd = "warsaw7mortar&canvas";
$mysqli = new mysqli($server, $user, $pwd, $dbName);
if ($mysqli->connect_errno) {
	echo "failure to connect";
	die('Connect Error: ' . $mysqli->connect_errno . ": " . $mysqli->connect_error);
}
else {
	$outActions = <<<END
					<p>
						<form action="https://spring-2022.cs.utexas.edu/cs329e-bulko/maxkret/HW16/insert.php">
							<button type="submit">Insert Student Record</button>
						</form>
					</p>
					<p>
						<form action="https://spring-2022.cs.utexas.edu/cs329e-bulko/maxkret/HW16/update.php">
							<button type="submit">Update Student Record</button>
						</form>
					</p>
					<p>
						<form action="https://spring-2022.cs.utexas.edu/cs329e-bulko/maxkret/HW16/delete.php">
							<button type="submit">Delete Student Record</button>
						</form>
					</p>
					<p>
						<form action="https://spring-2022.cs.utexas.edu/cs329e-bulko/maxkret/HW16/view.php">
							<button type="submit">View Student Record</button>
						</form>
					</p>
					<p>
						<form action="https://spring-2022.cs.utexas.edu/cs329e-bulko/maxkret/HW16/login.html">
							<button type="submit" onclick="alert('Thank You!')">Log Out</button>
						</form>
					</p>
					<br>
END;
	echo $outActions;
}
?>
					</span>
				</div>
			</div>
		</div>
	</div>
</body>
</html>