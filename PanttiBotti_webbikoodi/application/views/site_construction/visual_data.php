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
      <div class="row bg-primary w-50 offset-3" id="visual_data_box">

      </div>
    </div>
  <?php include 'footer.php'; ?>
  </body>
</html>
