<?php 
    require_once 'config/auth.php';
    if(connected()) {
        $lastname = $_SESSION['lastname'];
        $name = $_SESSION['name'];
        $birthday = $_SESSION['birthday'];
        $phone_number = $_SESSION['phone_number'];
        $mail = $_SESSION['mail'];
        $id = $_SESSION['id'];
    } else {
        header('Location: ../mysite/connexion.php');
        exit();
    };

    require_once("config/commandes.php");
    require_once("config/panier.php");

    $cart=afficherAllProduit($id);
    $items=afficher();
    $cart= $cart;

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Panier</title>
    <link rel="stylesheet" href="css/signin-login.css">
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.2.1/css/all.css">
</head>
<body>
    <?php require_once 'config/html/navbar.php';?>

<?php $i=0; foreach($items as $item):
            $i++;
            if(in_array("$i", $cart)){?>
    <div class="album py-5 bg-light">
    <div class="container">

    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
    <table class="table">
            <thead>
                <tr>
                <th scope="col">#</th>
                <th scope="col">image</th>
                <th scope="col">nom</th>
                <th scope="col">prix</th>
                <th scope="col">Description</th>
                <th scope="col">Ajouter/Retirer</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                <th scope="row"><?= $i ?></th>
                <td>
                <img src="<?= $item->image ?>" style="width: 15%; margin: auto;">
                </td>
                <td><?= $item->name ?></td>
                <td style="font-weight: bold; color: green;"><?= $item->price ?>€</td>
                <td><?= substr($item->description, 0, 100); ?>...</td>
                <td>Ajouter<br>Retirer</td>
                </tr>      
<?php } else {echo "Pas de produit";
};
endforeach; ?>

            </tbody>
            </table>
    </div>
</div>
</div>
</body>
</html>