<?php 

$q1 = $_REQUEST['q1'];
$q2 = $_REQUEST['q2'];
$q3 = $_REQUEST['q3'];
$q4 = $_REQUEST['q4'];
$q5 = $_REQUEST['q5'];
$q6 = $_REQUEST['q6'];
$score = 6;

if ( $q1 != 'false' ) {
	$score -= 1;
}

if ( $q2 != 'true' ) {
	$score -= 1;
}

if ( $q3 != 'b' ) {
	$score -= 1;
}

if ( $q4 != 'c' ) {
	$score -= 1;
}

if ( $q5 != 'http' ) {
	$score -= 1;
}

if ( $q6 != 'favicon' ) {
	$score -= 1;
}

echo $score;

?>