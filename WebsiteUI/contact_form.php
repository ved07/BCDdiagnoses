<?php

if(isset($_POST['submit'])){
    $name = $_POST['name'];
    $mailFrom = $_POST['mail'];
    $message = $_POST['message'];

    $mailTo = 'parimijash@gmail.com';
    $headers = "BCD Diagnosis Contact Form, From: ".$mailFrom;
    $txt = "You have received an e-mail from:".$name.".\n\n".$message;

    mail($mailTo, $txt, $headers);
    header("Location: index.html?mailsent");
}

?>