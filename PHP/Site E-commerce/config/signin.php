<?php 
if(isset($_POST['formsignin'])){
    extract($_POST);
    if(!empty($password) && !empty($cpassword) && !empty($mail)){
        if ($password == $cpassword){
            $options = ['cost' => 12,];
            $hashpass = password_hash($password, PASSWORD_BCRYPT, $options);
            
            include 'database.php';
            global $db;

            $c = $db->prepare("SELECT mail FROM user WHERE mail = :mail");
            $c->execute(['mail' => $mail]);
            $result = $c->rowCount();


            if($result == 0){
                $q = $db->prepare("INSERT INTO user(lastname,name,birthday,phone_number,mail,password) VALUES (:lastname,:name,:birthday,:phone_number,:mail,:password)");
                $q->execute([
                    'lastname' => $lastname,
                    'name' => $name,
                    'birthday' => $birthday,
                    'phone_number' =>$phone_number,
                    'mail' => $mail,
                    'password' => $hashpass
                ]);
                echo "Le compte a été créée, vous pouvez fermée la page.";
                session_start();
                $_SESSION['connected']= true;
                $_SESSION['lastname'] = $lastname;
                $_SESSION['name'] = $name;
                $_SESSION['birthday'] = $birthday;
                $_SESSION['phone_number'] = $phone_number;
                $_SESSION['mail'] = $mail;
                header('Location: ../mysite/dashboard.php');
                exit();
            } else {
                echo "Un email existe déjà !";
            }
        } else {
            echo "Les champs ne sont pas bons";
        }
    }
}

if(isset($_POST['formsetprofile'])){
    include 'database.php';
    global $db;
    $q = $db->query("SELECT * FROM user");
    $c = $db->prepare("SELECT mail FROM user WHERE mail = :mail");
    $c->execute(['mail' => $mail]);
    $result = $c->rowCount();
    extract($_POST);
    while ($user = $q->fetch()) { 
        if(!empty($password) && !empty($cpassword)){
            if ($password == $cpassword){
                $options = ['cost' => 12,];
                $hashpass = password_hash($password, PASSWORD_BCRYPT, $options);
                $q = $db->prepare("UPDATE user SET password = :password WHERE user.id = :id");
                $q->execute([
                    'id' => $user['id'],
                    'password' => $hashpass,
                ]);
            }
        }
        if  ($_SESSION['mail'] == $user['mail'] ) {
            $q = $db->prepare("UPDATE user SET lastname = :lastname, name = :name, birthday = :birthday, phone_number = :phone_number, mail = :mail WHERE user.id = :id");
            $q->execute([
                'id' => $user['id'],
                'lastname' => $lastname,
                'name' => $name,
                'birthday' => $birthday,
                'phone_number' => $phone_number,
                'mail' => $mail,
            ]);
            $_SESSION['connected']= true;
            $_SESSION['lastname'] = $lastname;
            $_SESSION['name'] = $name;
            $_SESSION['birthday'] = $birthday;
            $_SESSION['phone_number'] = $phone_number;
            $_SESSION['mail'] = $mail;
            header('Location: ../mysite/dashboard.php');
            exit();
        } else {
            if($result == 0){
                $q = $db->prepare("UPDATE user SET lastname = :lastname, name = :name, birthday = :birthday, phone_number = :phone_number, mail = :mail WHERE user.id = :id");
                $q->execute([
                    'id' => $user['id'],
                    'lastname' => $lastname,
                    'name' => $name,
                    'birthday' => $birthday,
                    'phone_number' => $phone_number,
                    'mail' => $mail,
                ]);
                $_SESSION['connected']= true;
                $_SESSION['lastname'] = $lastname;
                $_SESSION['name'] = $name;
                $_SESSION['birthday'] = $birthday;
                $_SESSION['phone_number'] = $phone_number;
                $_SESSION['mail'] = $mail;
                header('Location: ../mysite/dashboard.php');
                exit();
            } else {
                echo "Cet email est déjà utilisé !";
                exit();
            } 
        }
    }
}
?>