
<?php

if(isset($_POST["enter"])) {
    // open text file (writing emails to this for now)
    $text_file = fopen("contact_text.txt", "a");
    // assign user inputs to variables with line breaks
    $email = $_POST["email"] . "\n";
    $text_area = $_POST["text_area"] . "\n";
    // write to txt file
    fwrite($text_file, $email);
    fwrite($text_file, $text_area);
    fwrite($text_file, "----------\n");
    // close text file
    fclose($text_file);

    echo '<script type="text/javascript">';
    echo 'alert("Your message was successfully sent!")';
    echo '</script>';
    header("location: contactus.html");
}

?>