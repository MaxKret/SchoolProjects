
<!DOCTYPE html>
<html lang="en">

<head>
	<title>Online Signup Sheet</title>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="description" content="Online Signup Sheet">
	<meta name="author" content="Maxwell Kretschmer">
	<!-- <link rel="stylesheet" href="hw12.css"> -->
	<style>
		.flex-container {
			display: flex;
			justify-content: center;
		}
		.container {
			border: 2px solid;
			padding: 1em;
			margin: 1em;
		}
		caption {
			margin-bottom: 0.25cm;
		}
		#titleText {
			text-align: center;
			font-size: 3em;
			margin-bottom: 0em;
			margin-top: 0.25em;
		}
		td, th, caption {
			text-align: center;
			font-size: 2em;
		}
		input {
			width: 90%;
			margin: 2px;
		}
	</style>
</head>

<body>
	<h1 id="titleText"> Online Signup Sheet </h1>
	<form action="hw12.php/" method="POST" > <!-- http://www.cknuckles.com/cgi/echo.cgi -->
		<div class="flex-container">
			<div class="flex-conatiner">
				<div class="main">
					<div class="container">
						<?php
							// Read Signup.txt
							$filetable = array();
							if ($sf = fopen("signup.txt", "r")) {
								// $whole_file = fread($sf, filesize("signup.txt"));
								while (!feof($sf)) {
									$line = fgets($sf);
									if (strlen($line) > 2) {
										$tokens = explode(',', $line);
										$filetable[$tokens[0]] = rtrim($tokens[1]);
									}
								}
							}
							// echo "File: ";
							// echo print_r($filetable, true);
							// echo "\n";
							
							// Extract POST Vars
							// echo "POST: ";
							// echo print_r($_POST, true);
							// echo "\n";

							$myPostArr = array();
							$myPostArr['8am'] = rtrim($_POST['8am']);
							$myPostArr['9am'] = rtrim($_POST['9am']);
							$myPostArr['10am'] = rtrim($_POST['10am']);
							$myPostArr['11am'] = rtrim($_POST['11am']);
							$myPostArr['12pm'] = rtrim($_POST['12pm']);
							$myPostArr['1pm'] = rtrim($_POST['1pm']);
							$myPostArr['2pm'] = rtrim($_POST['2pm']);
							$myPostArr['3pm'] = rtrim($_POST['3pm']);
							$myPostArr['4pm'] = rtrim($_POST['4pm']);
							$myPostArr['5pm'] = rtrim($_POST['5pm']);
							
							// echo "myPOST: ";
							// echo print_r($myPostArr, true);
							// echo "\n";
							
							foreach ($myPostArr as $i => $value){
								if ($value != "") {
									$filetable[$i] = $value;
								}
							}
							
							// echo "Final File: ";
							// echo print_r($filetable, true);
							// echo "\n";

							// Write to Signup.txt
							if ($sf = fopen("signup.txt", "w")) {
								foreach ($filetable as $i => $value){
									$out = $i . "," . $value . "\n";
									$bytes_written = fwrite($sf, $out);
								}
							}

							// Update HTML
							$out8am = ($filetable['8am'] == "None") ? ('<input class="inputText" name="8am" type="text" />') : ($filetable['8am']);
							$out9am = ($filetable['9am'] == "None") ? ('<input class="inputText" name="9am" type="text" />') : ($filetable['9am']);
							$out10am = ($filetable['10am'] == "None") ? ('<input class="inputText" name="10am" type="text" />') : ($filetable['10am']);
							$out11am = ($filetable['11am'] == "None") ? ('<input class="inputText" name="11am" type="text" />') : ($filetable['11am']);
							$out12pm = ($filetable['12pm'] == "None") ? ('<input class="inputText" name="12pm" type="text" />') : ($filetable['12pm']);
							$out1pm = ($filetable['1pm'] == "None") ? ('<input class="inputText" name="1pm" type="text" />') : ($filetable['1pm']);
							$out2pm = ($filetable['2pm'] == "None") ? ('<input class="inputText" name="2pm" type="text" />') : ($filetable['2pm']);
							$out3pm = ($filetable['3pm'] == "None") ? ('<input class="inputText" name="3pm" type="text" />') : ($filetable['3pm']);
							$out4pm = ($filetable['4pm'] == "None") ? ('<input class="inputText" name="4pm" type="text" />') : ($filetable['4pm']);
							$out5pm = ($filetable['5pm'] == "None") ? ('<input class="inputText" name="5pm" type="text" />') : ($filetable['5pm']);

							$table = <<<END
							
							<table align="center" width="100%" border="2">
								<caption> Sign-Up Sheet </caption>
								<tr>
									<th> Time </th>
									<th> Name </th>
								</tr>
								<tr id="8am">
									<td class="timeLabel"> 8:00 am </td>
									<td class="nameLabel"> $out8am </td>
								</tr>
								<tr id="9am">
									<td class="timeLabel"> 9:00 am </td>
									<td class="nameLabel"> $out9am </td>
								</tr>
								<tr id="10am">
									<td class="timeLabel"> 10:00 am </td>
									<td class="nameLabel"> $out10am </td>
								</tr>
								<tr id="11am">
									<td class="timeLabel"> 11:00 am </td>
									<td class="nameLabel"> $out11am </td>
								</tr>
								<tr id="12pm">
									<td class="timeLabel"> 12:00 pm </td>
									<td class="nameLabel"> $out12pm </td>
								</tr>
								<tr id="1pm">
									<td class="timeLabel"> 1:00 pm </td>
									<td class="nameLabel"> $out1pm </td>
								</tr>
								<tr id="2pm">
									<td class="timeLabel"> 2:00 pm </td>
									<td class="nameLabel"> $out2pm </td>
								</tr>
								<tr id="3pm">
									<td class="timeLabel"> 3:00 pm </td>
									<td class="nameLabel"> $out3pm </td>
								</tr>
								<tr id="4pm">
									<td class="timeLabel"> 4:00 pm </td>
									<td class="nameLabel"> $out4pm </td>
								</tr>
								<tr id="5pm">
									<td class="timeLabel"> 5:00 pm </td>
									<td class="nameLabel"> $out5pm </td>
								</tr>
							</table>

END;

						echo $table;
						?>
					</div>
				</div>
			</div>
		</div>
		<div class="flex-container">
			<div class="flex-conatiner">
				<div class="main">
					<input type="submit" value="Submit" id="submit">
				</div>
			</div>
		</div>
	</form>

</body>

</html>