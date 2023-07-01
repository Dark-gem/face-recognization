
<?php
include 'connect.php';

session_start();

// <!-- initilizing variable name  -->

$username = $_POST['username'];
$password = $_POST['password'];




 $sql="select * from register where (username='$username' and password='$password')";
$result=mysqli_query($con,$sql);
  if(mysqli_num_rows($result) > 0){
        $_SESSION['logged_in'] = true;
        header("Location: user.php"); 
        die();
  }
  else{
        $_SESSION['message'] = "invalid credentials";
        header("Location: loginformhtml.php"); 
        die();
  }




?>