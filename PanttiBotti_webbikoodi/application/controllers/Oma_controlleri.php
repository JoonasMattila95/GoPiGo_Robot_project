<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Oma_controlleri extends CI_Controller {

	/**
	 * Index Page for this controller.
	 *
	 * Maps to the following URL
	 * 		http://example.com/index.php/welcome
	 *	- or -
	 * 		http://example.com/index.php/welcome/index
	 *	- or -
	 * Since this controller is set as the default controller in
	 * config/routes.php, it's displayed at http://example.com/
	 *
	 * So any other public methods not prefixed with an underscore will
	 * map to /index.php/welcome/<method_name>
	 * @see https://codeigniter.com/user_guide/general/urls.html
	 */
	public function index()
	{
		$this->load->view('login.php');
	}

	public function enter_mainpage()
	{
		$this->load->view('site_construction/main_site.php');
	}

	public function check_credentials(){
		$data['user_credentials']=$this->input->post();
		$this->load->model('Database_access');
		$validation = $this->Database_access->compare_credentials($data);
		if($validation == TRUE)
		{
			redirect(base_url().'/index.php/Oma_controlleri/enter_mainpage');
		}
		else {
			{
				redirect(base_url());
			}
		}
	}

	public function load_registeration_form()
	{
		$this->load->view('register_form');
	}

	public function add_user()
	{
		$data['new_user']=$this->input->post();
		$this->load->model('Database_access');
		$user_created = $this->Database_access->add_user_DB($data);
		if($user_created == TRUE)
		{
			redirect(base_url().'/index.php/Oma_controlleri/register_success');
		}
		else {
			redirect(base_url().'index.php/Oma_controlleri/load_registeration_form');
		}
	}

	public function register_success()
	{
	$this->load->view('register_successful');
}
}
