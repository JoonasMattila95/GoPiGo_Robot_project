<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
<link rel="stylesheet" href="<?php echo base_url();?>css/bootstrap.css">
    <link rel="stylesheet" type="text/css" href="<?php echo base_url();?>css/tyyli.css">
    <title>Uuden käyttäjän luonti</title>
  </head>
  <body>
    <div class="container bg-dark align-items-center">
      <div class="row w-50 bg-secondary">
      <form class="" action="<?php echo base_url()?>index.php/Oma_controlleri/add_user/" method="post">
          <label class="padder" for="username_label">Anna käyttäjänimi:</label><br>
          <input class="padder" type="text" name="username_input" size="50%" placeholder="username"><br>
          <label class="padder" for="password_label">Anna salasana:</label><br>
          <input class="padder" type="password" name="password_input" size="50%" placeholder="password"><br>
          <label class="padder" for="password_label">Anna salasana uudelleen:</label><br>
          <input class="padder" type="password" name="password_check" size="50%" placeholder="password"><br><br>
          <input class="padder" type="submit" name="sign_in" value="Luo käyttäjä"> <br><br>
      </form>
      </div>
    </div>

  </body>
</html>
