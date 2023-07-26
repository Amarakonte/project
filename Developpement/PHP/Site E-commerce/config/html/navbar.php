<?php
require_once dirname(__DIR__) . DIRECTORY_SEPARATOR . 'auth.php';
?>

<nav>
  <h1><a href="../mysite/index.php">Couwhainesihh</a></h1>
  <div class="onglets">
      <a href="../mysite/index.php">Nouveautés</a>
      <a href="#">Homme</a>
      <a href="#">Femme</a>
      <a href="#">Enfant</a>
      <a href="#">Cadeaux</a>
    <form>
      <input type="search" placeholder="Rechercher">
    </form>
    <a href="#"><i class="far fa-heart"></i></a>
    <a href="../mysite/cart.php"><i class="fas fa-shopping-cart"></i></a>
    <a href="../mysite/connexion.php"><i class="fa-solid fa-user"></i></a>
    <?php if(connected()): ?>
    <a href="../mysite/config/logout.php"><i class="fa-solid fa-right-from-bracket"></i></a> 
    <?php endif; ?>
  </div>
</nav>