<?php
class Database_access extends CI_Controller {

function compare_credentials($data)
{

  $this->load->database();

  $DB_username = $this->db->query('select password from user_info where username="'.$data['user_credentials']['username_input'].'"');
  $compared_username = $DB_username->row();
  if (isset($compared_username)){

    $DB_password = $compared_username->password;

    if($DB_password == $data['user_credentials']['password_input'])
      {
        session_start();
        $_SESSION['user'] = $data['user_credentials']['username_input'];
        return TRUE;
      }
    else {
      return FALSE;
    }
  }
  else
  {
    return FALSE;
  }

}

function add_user_DB($data)
{
  $this->load->database();

  $DB_username = $this->db->query('select password from user_info where username="'.$data['new_user']['username_input'].'"');
  $compared_username = $DB_username->row();
  if(isset($compared_username))
  {
    echo "käyttäjä on jo olemassa <br>";
    return FALSE;

  }
  else {
    if(strlen($data['new_user']['username_input']) < 6 )
    {
      echo "käyttäjänimi liian lyhyt";
      return FALSE;
    }
    else {

    if (strlen($data['new_user']['password_input']) < 8)
    {
      echo "salasana liian lyhyt";
      return FALSE;

    }
    else {
      if ($data['new_user']['password_input'] == $data['new_user']['password_check'])
      {
      echo "kaikki buenoo";
      $is_successful = $this->db->query("insert into user_info values('".$data['new_user']['username_input'].
      "','".$data['new_user']['password_input']."')");
      if ($is_successful == TRUE)
      {
        echo "käyttäjä lisätty";
        return TRUE;
      }
      else {
        echo "Jotain meni pieleen SQL puolella";
      }
      }
    else {
      echo "kirjotit salasanasi tarkistuksen väärin pälli";
      return FALSE;

    }
  }
  }
  }
}
<<<<<<< Updated upstream
=======

function fetch_data()
{
  $this->load->database();

  $DB_log = $this->db->query('select * from ajodata ');
  $DB_log = $DB_log->result();
  return $DB_log;
}


>>>>>>> Stashed changes
}

?>
