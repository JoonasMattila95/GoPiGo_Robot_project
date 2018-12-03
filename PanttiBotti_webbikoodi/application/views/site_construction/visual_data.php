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
      <div class="row bg-secondary w-25 offset-4">
        <img src="<?php echo base_url(); ?>images/happy_hedgehog.jpg" alt="hilpee siili">
      </div>
      <div class="row bg-secondary w-25 offset-4 up_padder">
          <h1> No data here, just a hedgehog </h1>
      </div>
    </div>
  <?php include 'footer.php'; ?>
  </body>
</html>
