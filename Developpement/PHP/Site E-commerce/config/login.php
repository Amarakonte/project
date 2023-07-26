<?php
    if(isset($_POST['formlogin'])){
        extract($_POST);
        include 'database.php';
        global $db; 
        if(!empty($lmail) && !empty($lpassword)){
            $q = $db->prepare("SELECT * FROM user WHERE mail = :mail");
            $q->execute(['mail' => $lmail]);
            $result = $q->fetch();

            if($result == true){
                //Le compte existe bien
                $hashpassword = $result['password'];
                if(password_verify($lpassword, $hashpassword)){
                    echo "Le mot de passe est bon, connection en cours";
                    if (!empty($lcookie)){
                        setcookie('lmail',$result['mail'], time()+ (30*24*3600));
                        $_COOKIE[$lcookie] = $result['mail'];
                    } else {
                        setcookie('lmail','',time());
                    }
                    session_start();
                    $_SESSION['connected']= true;
                    $_SESSION['lastname'] = $result['lastname'];
                    $_SESSION['name'] = $result['name'];
                    $_SESSION['birthday'] = $result['birthday'];
                    $_SESSION['phone_number'] = $result['phone_number'];
                    $_SESSION['mail'] = $result['mail'];
                    $_SESSION['id'] = $result['id'];
                    header('Location: ../mysite/dashboard.php');
                    exit();
                } else {
                    echo "Le mot de passe est incorrecte, réessayer";
                }
            } else {
                echo "Le compte portant l'email " . $lmail . " n'existe pas";
            }
            
        } else {
            echo "Veuillez completer l'ensemble des champs";
        }
    }
?>