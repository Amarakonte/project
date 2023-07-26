<?php
    require_once 'config/auth.php';
    if(connected()) {
        header('Location: ../mysite/dashboard.php');
        exit();
    };
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Connexion</title>
    <link rel="stylesheet" href="css/signin-login.css">
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.2.1/css/all.css">
</head>
<body>
    <?php require_once 'config/html/navbar.php';?>
    <form method="post" class="border" action="">
        <h2>Login</h2>
        <input type="email" name="lmail" id="lmail" placeholder="Votre email" value="<?php if(!empty($_COOKIE['lmail'])){echo $_COOKIE['lmail'];}?>" required>
        <input type="password" name="lpassword" id="lpassword" placeholder="Mot de passe" required>
        <p><input type="checkbox" name="lcookie" id="lcookie" <?php if(!empty($_COOKIE['lmail'])){?>checked<?php };?>> Se rappeler de moi</p>
        <input class=formsend type="submit" name="formlogin" id="formlogin" value="Connexion">
        <p>Vous n'êtes pas encore inscrit ? <a href="inscription.php">Inscrivez Vous</a></p>
    </form>
    <?php require_once 'config/login.php'; ?>
</body>
</html>