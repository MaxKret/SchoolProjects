<?php
   session_start();
?>

<!DOCTYPE html>
<html>
<body>

<?php
   echo "The university is " . $_SESSION["univ"] . ".<br>";
   echo "The mascot is " . $_SESSION["mascot"] . ".<br>";
?>

</body>
</html>