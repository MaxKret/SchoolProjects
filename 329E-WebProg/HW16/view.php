<!DOCTYPE html>
<html lang="en">

<head>
	<title>View</title>
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
				<h2> View </h2>
				<div class="centering-container">
					<div class="logregContainer">
						<form method="POST">
							<p>
								<label>ID:</label>
								<input name="g_id" id="g_id" type="text" />
							</p>
							<p>
								<label>Last Name:</label>
								<input name="g_last" id="g_last" type="text"/>
							</p>
							<p>
								<label>First Name:</label>
								<input name="g_first" id="g_first" type="text"/>
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
$g_id = $_POST['g_id'];
$g_id = ($g_id === "") ? NULL : $g_id;
$g_last = $_POST['g_last'];
$g_last = ($g_last === "") ? NULL : $g_last;
$g_first = $_POST['g_first'];
$g_first = ($g_first === "") ? NULL : $g_first;


function get_querytext($varset, $g_ID = NULL, $g_LAST = NULL, $g_FIRST = NULL)
{
	switch ($varset) {
		case ["false", "false", "false"]:
			$queryT = "error";
			break;
		case ["false", "false", "true"]:
			$queryT = "SELECT * FROM STUDENTS " .
				"WHERE FIRSTNAME = \"$g_FIRST\";";
			break;
		case ["false", "true", "false"]:
			$queryT = "SELECT * FROM STUDENTS " .
				"WHERE LASTNAME = \"$g_LAST\";";
			break;
		case ["false", "true", "true"]:
			$queryT = "SELECT * FROM STUDENTS " .
				"WHERE LASTNAME = \"$g_LAST\" AND " .
				"FIRSTNAME = \"$g_FIRST\";";
			break;
		case ["true", "false", "false"]:
			$queryT = "SELECT * FROM STUDENTS " .
				"WHERE ID = \"$g_ID\";";
			break;
		case ["true", "false", "true"]:
			$queryT = "SELECT * FROM STUDENTS " .
				"WHERE ID = \"$g_ID\" AND " .
				"FIRSTNAME = \"$g_FIRST\";";
			break;
		case ["true", "true", "false"]:
			$queryT = "SELECT * FROM STUDENTS " .
				"WHERE ID = \"$g_ID\" AND " .
				"LASTNAME = \"$g_LAST\";";
			break;
		case ["true", "true", "true"]:
			$queryT = "SELECT * FROM STUDENTS " .
				"WHERE ID = \"$g_ID\" AND " .
				"LASTNAME = \"$g_LAST\" AND " .
				"FIRSTNAME = \"$g_FIRST\";";
			break;
		default:
			$queryT = "error";
			break;
	}
	return $queryT;
}
$varset_arr = array(
	isset($g_id) ? 'true' : 'false',
	isset($g_last) ? 'true' : 'false',
	isset($g_first) ? 'true' : 'false'
);
if ($varset_arr === ["false", "false", "false"]) {
	if (isset($_POST["viewAll"])) {
		$query = $mysqli->query("SELECT * FROM STUDENTS ORDER BY LASTNAME,FIRSTNAME");
		if (!$query) {
			echo "Error";
			die("Query failed: ($mysqli->error <br> SQL command = $query");
		}
		else 
		{
			// DISPLAY RECORD
			$table = <<<END
				<table align="center" width="100%" border="1">
					<caption> STUDENTS </caption>
					<tr>
						<th> ID </th>
						<th> LAST </th>
						<th> FIRST </th>
						<th> MAJOR </th>
						<th> GPA </th>
					</tr>\n
END;
			$table_end = <<<END
				
			</tr>
			</table>
END;

			while ($record = $query->fetch_row()) {
				$r_ID = $record[0];
				$r_LAST = $record[1];
				$r_FIRST = $record[2];
				$r_MAJOR = $record[3];
				$r_GPA = $record[4];
		
				$t_row = <<<END
					<tr>
						<td> $r_ID </td>
						<td> $r_LAST </td>
						<td> $r_FIRST </td>
						<td> $r_MAJOR </td>
						<td> $r_GPA </td>
					</tr>
END;
				$table = $table . $t_row;
			}
			$table = $table . $table_end;
			
			echo $table;
		}
	}
}
else {
	// GET RECORD
	$query_text = get_querytext($varset_arr, $g_id, $g_last, $g_first);
	if ($query_text !== "error") {
		$query = $mysqli->query($query_text);
	}

	if (!$query) {
		echo "Error";
		die("Query failed: ($mysqli->error <br> SQL command = $query");
	}
	else {
		// DISPLAY RECORD
		$_match = false;
		$table = <<<END
			<table align="center" width="100%" border="1">
				<caption> STUDENTS </caption>
				<tr>
					<th> ID </th>
					<th> LAST </th>
					<th> FIRST </th>
					<th> MAJOR </th>
					<th> GPA </th>
				</tr>\n
END;
		$table_end = <<<END
			
		</tr>
		</table>
END;

		while ($record = $query->fetch_row()) {
			$_match = true;
			$r_ID = $record[0];
			$r_LAST = $record[1];
			$r_FIRST = $record[2];
			$r_MAJOR = $record[3];
			$r_GPA = $record[4];
	
			$t_row = <<<END
				<tr>
					<td> $r_ID </td>
					<td> $r_LAST </td>
					<td> $r_FIRST </td>
					<td> $r_MAJOR </td>
					<td> $r_GPA </td>
				</tr>
END;
			$table = $table . $t_row;
		}
		$table = $table . $table_end;
		
		if ($_match) {
			echo $table;
		}
		else {
			echo "No Matches \n";
		}
	}
}
?>
						</span>
					</div>
				</div>
				<br>
				<br>
				<div class="centering-container">
					<form method="POST">
						<button type="submit" name="viewAll" id="viewAll">View All Student Records</button>
					</form>
				</div>
			</div>
		</div>
	</div>
</body>

</html>
