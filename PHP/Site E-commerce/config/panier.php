<?php


function modifierP($idItem, $quantity, $idUser)
{
    if ($quantity == 0) {
        $db=new pdo("mysql:host=localhost;dbname=projet_sql;charset=utf8", "root", "");
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
        $req=$db->prepare("DELETE FROM cart WHERE idUser=? AND idItem=?");
        $req->execute(array($idUser, $idItem));
        $req->closeCursor();
    } else {
        $db=new pdo("mysql:host=localhost;dbname=projet_sql;charset=utf8", "root", "");
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
        $req = $db->prepare("UPDATE cart SET idItem = ?, quantity = ? WHERE idUser=?");
        $req->execute(array($idItem, $quantity, $idUser));
        $req->closeCursor();
    }
}


function afficherProduit($idUser)
{
	if(require_once("database.php"))
	{
		$req=$db->prepare("SELECT idItem FROM cart WHERE idUser=?");

        $req->execute(array($idUser));

        $data = $req->fetchAll(PDO::FETCH_OBJ);

        return $data;

        $req->closeCursor();
	}
}

  function ajouterP($idItem, $quantity, $idUser)
  {
    if(require_once("database.php"))
    {
      $db=new pdo("mysql:host=localhost;dbname=projet_sql;charset=utf8", "root", "");
      $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
      $req=$db->prepare("SELECT idItem FROM cart WHERE idUser=?");
      $req->execute(array($idUser));

      $req = $db->prepare("INSERT INTO cart (idItem, quantity, idUser) VALUES (?, ?, ?)");

      $req->execute(array($idItem, $quantity, $idUser));

      $req->closeCursor();
      echo "Cela a bien été ajouté dans le panier";
      
    }
  }



function supprimerAll($idUser)
{
  $db=new pdo("mysql:host=localhost;dbname=projet_sql;charset=utf8", "root", "");
  $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
  $req=$db->prepare("DELETE FROM cart WHERE idUser=?");
  $req->execute(array($idUser));
  $req->closeCursor();
}

?>