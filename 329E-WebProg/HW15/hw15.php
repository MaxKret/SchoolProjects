<?php 
session_start();

$idx = $_REQUEST['idx'];
$ans = $_REQUEST['ans'];
$user = $_SESSION['loggedin'];
$score = 0;

$answers = array("0" => 'false',"1" => 'true',"2" => 'b',"3" => 'c',"4" => 'http',"5" => 'favicon');

function tailFile($lines = 1) {
	return trim(implode("", array_slice(file("results.txt"), -$lines)));
}

if ( $ans != $answers[$idx] ) {
	$score = 0;
}
else {
	$score = 10;
}

if ($fh = fopen("results.txt", "r")) {
	$whole_file = fread($fh, filesize("results.txt"));
	if (substr_count($whole_file, $user) >= 1) {
		fclose($fh);
		if ($fr = fopen("results.txt", "r")) {
			$line = rtrim(tailFile());
			fclose($fr);
			$read_score = substr($line, strpos($line, ":")+1);
			$score = $read_score + $score;
			if ($fw = fopen("results.txt", "a")) {
				fwrite($fw, "$user:$score \n");
				fclose($fw);
			}
		}
	}
	else{
		fclose($fh);
		if ($fw = fopen("results.txt", "a")) {
			fwrite($fw, "$user:$score \n");
			fclose($fw);
		}
	}
}
else {
	echo "error: no file found";
}
if ($idx === "5") {
	echo $score;
}
else {
	echo "read score: " . $read_score . " question score: ". $score;
}

?>