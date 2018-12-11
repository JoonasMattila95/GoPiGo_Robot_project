<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="<?php echo base_url();?>css/bootstrap.css">
    <link rel="stylesheet" type="text/css" href="<?php echo base_url();?>css/tyyli.css">
    <title>PanttiBotti_Login</title>
  </head>
  <body>
    <div class="container bg-dark">
      <div class="login_row w-25">
      <form class="bg-secondary " action="<?php echo base_url()?>index.php/Oma_controlleri/check_credentials/" method="post">
        <label class="padder" for="username_label">Käyttäjänimi:</label><br>
        <input class="padder" type="text" name="username_input" placeholder="username"><br>
        <label class="padder" for="password_label">Salasana:</label><br>
        <input class="padder" type="password" name="password_input" placeholder="password"><br><br>
        <input class="padder" type="submit" name="sign_in" value="Sign in"> <br><br>
      </div>
      </form>
      <div class = "row" id ="new_user_button">
        <a href ="<?php echo base_url().'index.php/Oma_controlleri/load_registeration_form'?>"> Luo uusi käyttäjä </a>
      </div>
    </div>
  </body>
</html>
