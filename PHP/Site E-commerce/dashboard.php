<?php 
    require_once 'config/auth.php';
    if(!connected()) {
        header('Location: ../mysite/connexion.php');
        exit();
    };
    $lastname = $_SESSION['lastname'];
    $name = $_SESSION['name'];
    $birthday = $_SESSION['birthday'];
    $phone_number = $_SESSION['phone_number'];
    $mail = $_SESSION['mail'];
    if (!empty($_SESSION['id'])){
        $id = $_SESSION['id'];
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profil</title>
    <link rel="stylesheet" href="css/signin-login.css">
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.2.1/css/all.css">
</head>
<body>
    <?php require_once 'config/html/navbar.php'; ?>
    <div class="container d-flex justify-content-center">
        <div class="card p-3 py-4">
            <div class="text-center">
                <h3 class="Prenom">Vos informations</h3>
                <p class="profession"><?= $name; ?> <?= $lastname; ?></p>
                <br>
                <div class="EnsembleProfile">
                    <div class="infos">
                        <h5>date de naissance</h5>
                        <span class="num"><?= $birthday; ?></span>
                    </div>
                    <br>
                    <div class="infos">
                        <h5>Téléphone</h5>
                        <span class="num"><?= $phone_number; ?></span>
                    </div>
                    <br>
                    <div class="infos">
                        <h5>Email</h5>
                        <span class="num"><?= $mail; ?></span>
                    </div>
                </div>
                <br>
                <button class="profile_button" onclick="window.location.href ='parametre.php';">Modifier vos paramètres</button>
            </div>
        </div>
    </div>
    <div class="container d-flex justify-content-center">
        <div class="card p-3 py-4">
            <div class="text-center">
                <h3 class="Prenom">Vos produits</h3>
                <br>
                <button class="profile_button" onclick="window.location.href ='admin/index.php';">Accéder à vos produits</button>
            </div>
        </div>
    </div>
</body>
</html>