<?php
session_start();
session_unset($_SESSION['connected']);
session_destroy();
header('Location: ../index.php');
