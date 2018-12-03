<!DOCTYPE html>
<?php include 'topbar.php';
session_start();
if(is_null($_SESSION['user']) == TRUE)          //Check if user has logged in
{
    redirect(base_url());
}
?>

<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Ajodata</title>
  </head>
  <body>
    <div class="bg-dark" id="main_page">
      <div class="row offset-5  w-25" id="scrollable">
        <ul class="data_list">
          <?php
            foreach ($drive_data as $value) {
              echo "<li>".$value->komento."<br>";
              echo $value->timestamp."</li>";}?>
        </ul>
      </div>
    </div>
  <?php include 'footer.php'; ?>
  </body>
</html>
