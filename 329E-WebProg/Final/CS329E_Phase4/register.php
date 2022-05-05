<?php
# get the incoming information
$name = $_REQUEST["user"];
$email = $_REQUEST["email"];


# open file 'info.txt' and append the name and e-mail address
if ($fh = fopen("users.txt", "a")) {
	fwrite($fh, "$name  $email \n");
	fclose($fh);
}
if ($fh = fopen("emails.txt", "a")) {
	fwrite($fh, "$email \n");
	fclose($fh);
}

# Write thank you page
$a = file_get_contents("successful_register.html");
$b = str_replace("NotAvailable", $email, $a);
$c = str_replace('<!DOCTYPE html>', "", $b);
$d = str_replace('<html lang="en">', "", $c);
$contents = str_replace('</html>', "", $d);
echo $contents;
?>