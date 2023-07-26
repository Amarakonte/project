<?php 
    require_once 'config/auth.php';
    if(connected()) {
        header('Location: ../mysite/dashboard.php');
        $lastname = $_SESSION['lastname'];
        $name = $_SESSION['name'];
        $birthday = $_SESSION['birthday'];
        $phone_number = $_SESSION['phone_number'];
        $mail = $_SESSION['mail'];
        $id = $_SESSION['id'];
        exit();
    };
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inscription</title>
    <link rel="stylesheet" href="css/signin-login.css">
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.2.1/css/all.css">
</head>
<body>
    <?php require_once 'config/html/navbar.php';?>
    <form method="post" class="border" action="">
        <h2>Inscription</h2>
        <input type="text" name="lastname" id="lastname" placeholder="Votre nom" required>
        <input type="text" name="name" id="name" placeholder="Votre prénom" required>
        <input type="date" name="birthday" id="birthday" placeholder="Votre date de naissance" required>
        <input type="text" id="phone_number" name="phone_number" placeholder="Votre numéro de téléphone" required>
        <input type="email" name="mail" id="mail" placeholder="Votre email" required>
        <input type="password" name="password" id="password" placeholder="Votre mot de passe" required>
        <input type="password" name="cpassword" id="cpassword" placeholder="Confirmer mot de passe" required>
        <input class="formsend" type="submit" name="formsignin" id="formsignin" value="Inscription">
    </form>
    <?php require_once 'config/signin.php'; ?>
</body>
</html>