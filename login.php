
<!DOCTYPE html>
<html lang="en">
    
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login form</title>
    <link rel="stylesheet" href="loginpage.css">
   <?php
        session_start();
   
   ?>
<script >
    function validateform(){  
        event.preventDefault();
        if (myform.username.value==""){  
       alert("Username  can't be blank");  
       myform.username.focus();
       return false;  
        }
       if (myform.password.value==""){  
       alert("password  can't be blank");  
       myform.password.focus();
       return false;
    } 
    document.getElementById('form1').submit();
        
    }
    
</script> 
<style>
    body
    {
        background-image: url(login.jpg);
        background-repeat: no-repeat;
        background-position: center;
        background-size:cover;
    }
    .centre{
        background-color: antiquewhite;
    }
    .centre .inputfield .inputbox
    {
        height: 25px;
        width: 200px;
        margin: 10px;
        outline: none;
        padding-left: 7px;
        border: 1px solid #ccc;
        border-bottom-width: 2px;
    }
    .submitbtn
    {
        align-items: center;
    }
    .submits
    {
        background-color: aquamarine;
        border-radius: 30px;
        margin: 10px;
        margin-left: 60px;
        cursor: pointer;
    }
    .signup_link{
        color: orange;
        border-radius: 30px;
        padding-left:10px ;
        cursor: pointer;
        text-align: center;
        margin-left: 200px;
        border: none;
        background-color:antiquewhite ; 
        font-size: medium;
    }
    .signup_link:hover{
        color: red;
    }

</style>


</head>
<body>
    <div class="centre">
        <h1>Login Form</h1>
        <form method="post" name="myform"   action="connectdb.php" id="form1" onsubmit="validateform()">
            <div class="inputfield" id="username">
                <label>Username :</label>
            <input class="inputbox" type="text" name="username" >
         
            </div>
            <div class="inputfield" id="password">
                <label>Password :</label>
                <input class="inputbox" type="password" name="password" >
             
            </div>
            <div class="submitbtn">
            <input class="submits" type="submit" value="Submit">
            </div>
          </form>
        <div class="forsignup">
        <div class="link">
      <!-- <a href="registerpagehtml.php"> -->
        Click Here for signup page
   </a>
    </div>
            </div>
            <div>
                
            </div>
            <?php 
                 if(isset($_SESSION['message']))
                 {
                     echo $_SESSION['message'];
                     unset($_SESSION['message']);
                 }
            ?>
    </div>
  
</body>
</html>