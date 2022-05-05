// AJAX
$(function () {
	$("#user").keyup(function () {
		validate_user();
	});
	$("#user").change(function () {
		prev_username();
	});
	$("#pass1").keyup(function () {
		validate_password1();
	});
	$("#pass1").change(function () {
		validate_password1();
	});
	$("#pass2").keyup(function () {
		validate_password2();
	});
	$("#pass2").change(function () {
		validate_password2();
	});
});


// VARS
var _prevExists = false;
var _badUser = false;
var _badPass1 = false;
var _badPass2 = false;
var useremail;
var user;
var pass1;
var pass2;
var loginpage = "https://spring-2022.cs.utexas.edu/cs329e-bulko/maxkret/HW14/login.html";


// HELPER METHODS
function changeRed(target) {
	target.style.color = "red";
}
function changeBlack(target) {
	target.style.color = "black";
}
function changeWhite(target) {
	target.style.color = "white";
}
function changeBold(target) {
	target.style.fontWeight = "bold";
}
function changeBack(target) {
	target.style.fontWeight = 'normal';
}


// VALIDATION
function prev_username() {
	prevuser_e = document.getElementById("user");
	prevuserval = prevuser_e.value;
	prevuser_label = document.getElementById("lableu");

	const xhttp_prev_user = new XMLHttpRequest();
	xhttp_prev_user.open(
		"GET",
		"prev_user.php?prevuser=" + prevuserval,
		false
	);
	xhttp_prev_user.send();
	_isNew = xhttp_prev_user.responseText;

	console.log(prevuserval + " is new: " + _isNew);
	if (_isNew === "false") {
		
		_prevExists = true;
	}
	else if (_isNew === "true") {
		
		_prevExists = false;
	}
	else {
		console.log(_isNew);
	}
}

function validate_user() {

	regex_alphanum_user = /^[A-Za-z][a-zA-Z0-9]{5,9}$/;
	user = document.getElementById("user");
	user_label = document.getElementById("labelu");

	if (!(user.value.match(regex_alphanum_user))) {
		changeRed(user);
		changeRed(user_label);
		changeBold(user_label);
		console.log(user.value + " is not valid");
		_badUser = true;
		return false;
	}
	else {
		changeBlack(user);
		changeWhite(user_label);
		changeBack(user_label);
		console.log(user.value + " is valid");
		_badUser = false;
		return true;
	}
}

function validate_password1() {
	// VARS
	regex_alphanum = /^[A-Za-z0-9][a-zA-Z0-9]{5,9}$/;
	regex_atleast = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,10}$/;
	pass1 = document.getElementById("pass1");
	pass1_label = document.getElementById("labelp1");

	if (!(pass1.value.match(regex_alphanum) && pass1.value.match(regex_atleast))) {
		changeRed(pass1);
		changeRed(pass1_label);
		changeBold(pass1_label);
		console.log(pass1.value + " is not valid");
		_badPass1 = true;
		return false;
	}
	else {
		changeBlack(pass1);
		changeWhite(pass1_label);
		changeBack(pass1_label);
		console.log(pass1.value + " is valid");
		_badPass1 = false;
		return true;
	}
}

function validate_password2() {
	pass2 = document.getElementById("pass2");
	pass2_label = document.getElementById("labelp2");

	if (pass1.value != pass2.value) {
		changeRed(pass2);
		changeRed(pass2_label);
		changeBold(pass2_label);
		console.log(pass2.value + " does not match");
		_badPass2 = true;
		return false;
	}
	else {
		changeBlack(pass2);
		changeWhite(pass2_label);
		changeBack(pass2_label);
		console.log(pass2.value + " matches");
		_badPass2 = false;
		return true;
	}
}


function validate() {
	if (_prevExists || _badUser || _badPass1 || _badPass2) {
		alert("Invalid email, username, or password");
	}
	else {
		const xhttp_register = new XMLHttpRequest();
		xhttp_register.open(
			"GET",
			"register.php?user=" + prevuserval + "&pass=" + pass1.value,
			false
		);
		xhttp_register.send();

		const xhttp_seshmanager_cookie_set = new XMLHttpRequest();
		xhttp_seshmanager_cookie_set.open(
			"GET",
			"seshmanager.php?op=set&key=cookie&val=" + prevuserval,
			false
		);
		xhttp_seshmanager_cookie_set.send();

		const xhttp_seshmanager_loggedin_set = new XMLHttpRequest();
		xhttp_seshmanager_loggedin_set.open(
			"GET",
			"seshmanager.php?op=set&key=loggedin&val=true",
			false
		);
		xhttp_seshmanager_loggedin_set.send();

		const xhttp_seshmanager_redir_get = new XMLHttpRequest();
		xhttp_seshmanager_redir_get.open(
			"GET",
			"seshmanager.php?op=get&key=redirect",
			false
		);
		xhttp_seshmanager_redir_get.send();

		let redir_href = xhttp_seshmanager_redir_get.responseText;
		if (redir_href === loginpage) {
			window.location.href = "https://spring-2022.cs.utexas.edu/cs329e-bulko/maxkret/HW14/hw14.html"
		}
		else {
			window.location.href = redir_href;
		}
	}
}