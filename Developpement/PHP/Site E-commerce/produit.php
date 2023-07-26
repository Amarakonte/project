<?php

require_once("config/commandes.php");
require_once("config/panier.php");

$items=afficher();

if(isset($_GET['pdt'])){
    
    if(!empty($_GET['pdt']) OR is_numeric($_GET['pdt']))
    {
        $id = $_GET['pdt'];

    }
} ?>

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
        <?php foreach($items as $item){ if($item->id == $id){ ?> 
        <div class="col-md-8">
            <div class="card shadow-sm" >
                <form action="" method="post">
                <h3 align="center"><?= $item->name ?></h3>
                <img src="<?= $item->image ?>" style="width: 50%">

                <div class="card-body">
                <p class="card-text"><?= $item->description ?></p>
                <div class="d-flex justify-content-between align-items-center">
                    <div class="btn-group">
                    <input class="formsend" type="submit" name="formaddcart" id="formaddcart" value="Commander">
                    </div>
                    <small class="text" style="font-weight: bold;"><?= $item->price ?> €</small>
                </div>
                </div>
                </form>
            </div>
            </div>
        <?php }} ?>
        </div>
    </div>
</body>
</html>
<?php
    if(isset($_POST['formaddcart'])){
        ajouterP($id,1,$_SESSION['id']);
    }
?>