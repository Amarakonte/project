<?php

$header="MIME-Version: 1.0\r\n";
$header.= 'From: "Couwhainesihh.com"<delafontainecouwhainesihh@couwhainesihh.com>'."\n";
$header.= 'Content-Type:text/html; charset="UTF-8"'."\n";
$header.= 'Content-Transfer-Encoding: 8bit';

$message='
<html>
    <body>
        <div align="center">
            <h1>J\'ai envoyé ce mail avec PHP</h1>
            <br>
            <img src="https://images.sftcdn.net/images/t_app-cover-l,f_auto/p/ce2ece60-9b32-11e6-95ab-00163ed833e7/260663710/the-test-fun-for-friends-screenshot.jpg" alt="">
        </div>
    </body>
</html>
';

if (mail("amara.konte@ynov.com", 'Salut test', $message, $header)){
    echo "Envoyer";
} else {
    echo "Erreur test";
}
?>