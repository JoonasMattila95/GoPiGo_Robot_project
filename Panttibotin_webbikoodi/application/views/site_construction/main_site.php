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
    <title>Panttibotti_etusivu</title>
  </head>
  <body>
    <div class="bg-dark" id="main_page">
      <div class="row offset-3 bg-secondary w-50">
    <?php echo'<h1> Tervetuloa Panttibotin etusivulle '.$_SESSION['user'].' </h1>'; ?>
      </div>
    </div>
  <?php include 'footer.php'; ?>
  </body>
</html>
