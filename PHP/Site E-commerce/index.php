<?php session_start();

require_once("config/commandes.php");

  $items=afficher();

?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Couwhainesihh Corporation</title>
  <link rel="stylesheet" href="css/main.css">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.2.1/css/all.css">
</head>
<body>
  <!-- Barre de navigation -->
  <?php require_once 'config/html/navbar.php';?>
  <!-- Fin de la barre de navigation -->
  
  <!-- Header -->
   <header>
     <h1>C'est votre kwencyquence, votre achat.</h1>
     <a href="#main"><button>Naviguer <i class="fas fa-paper-plane"></i></button></a>
   </header>
  <!-- Fin du header -->
  
  <!-- Section principale -->
  <section id="main" class="main">
    
    <!-- Toutes les cartes -->

    <div class="cards">
    <?php foreach($items as $item): ?> 
      <div class="card">
        <a href="produit.php?pdt=<?= $item->id ?>">
        <img src="<?= $item->image ?>">
        <div class="card-header">
          <h4 class="title"><?= $item->name ?></h4>
          <h4 class="price"><?= $item->price ?></h4>
        </div>
        <div class="card-body">
          <p><?= $item->description ?></p>
        </div>
        </a>
      </div>
    <?php endforeach; ?>
     </div>
    <!-- Fin de toutes les cartes -->
    
  </section>
  <!-- Fin de la section principale -->
  
  <!-- Pied de page -->
  <footer>
    <p>&copy; Contactez-nous au 06 98 87 82 00</p>
    <div class="social-media">
      <p><i class="fab fa-facebook-f"></i></p>
      <p><i class="fab fa-twitter"></i></p>
      <p><i class="fab fa-instagram"></i></p>
      <p><i class="fab fa-linkedin-in"></i></p>
    </div>
  </footer>
  <!-- Fin du pied de page -->
</body>
</html>