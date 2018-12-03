<?php
  session_start();
  session_destroy();
 ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="<?php echo base_url();?>css/bootstrap.css">
    <link rel="stylesheet" type="text/css" href="<?php echo base_url();?>css/tyyli.css">
    <title>Kirjauduit ulos</title>
  </head>
  <body>
    <div class="container bg-dark">
      <div class="row  w-75 bg-secondary align-self-center">
        <div class="col-md offset-4">
            <h1> Kirjauduit ulos </h1>
        </div>
      </div>
      <div class="row up_padder w-50  align-self-center ">
        <div class="col-md offset-4">
            <a href="<?php echo base_url();?>index.php/Oma_controlleri/index "> Palaa kirjautumissivulle</a>
        </div>
      </div>
    </div>
  </body>
</html>
