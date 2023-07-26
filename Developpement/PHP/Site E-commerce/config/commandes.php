<?php


function modifier($name, $image, $price, $description, $stock, $category, $id)
{
  $db=new pdo("mysql:host=localhost;dbname=projet_sql;charset=utf8", "root", "");
  $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
  $req = $db->prepare("UPDATE product SET  name = ?, image = ?, price = ?, description = ?, stock = ?, category = ? WHERE id=?");
  $req->execute(array($name, $image, $price, $description, $stock, $category, $id));
  $req->closeCursor();
}


function afficherUnProduit($id)
{
	if(require_once("database.php"))
	{
		$req=$db->prepare("SELECT * FROM product WHERE id=?");

        $req->execute(array($id));

        $data = $req->fetchAll(PDO::FETCH_OBJ);

        return $data;

        $req->closeCursor();
	}
}

function afficherAllProduit($idUser)
{
	if(require_once("database.php"))
	{
		$req=$db->prepare("SELECT * FROM product WHERE idUser=?");

        $req->execute(array($idUser));

        $data = $req->fetchAll(PDO::FETCH_OBJ);

        return $data;

        $req->closeCursor();
	}
}

  function ajouter($name, $image, $price, $description, $stock, $category, $idUser)
  {
    if(require_once("database.php"))
    {
      $req = $db->prepare("INSERT INTO product (name, image, price, description, stock, category, idUser) VALUES (?, ?, ?, ?, ?, ?, ?)");

      $req->execute(array($name, $image, $price, $description, $stock, $category, $idUser));

      $req->closeCursor();
    }
  }

function afficher()
{
	if(require_once("database.php"))
	{
    $db=new pdo("mysql:host=localhost;dbname=projet_sql;charset=utf8", "root", "");
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
		$req=$db->prepare("SELECT * FROM product ORDER BY id DESC");

        $req->execute();

        $data = $req->fetchAll(PDO::FETCH_OBJ);

        return $data;

        $req->closeCursor();
	}
}

function supprimer($id)
{
  $db=new pdo("mysql:host=localhost;dbname=projet_sql;charset=utf8", "root", "");
  $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
  $req=$db->prepare("DELETE FROM product WHERE id=?");
  $req->execute(array($id));
  $req->closeCursor();
}

?>