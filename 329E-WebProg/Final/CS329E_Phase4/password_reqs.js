// AJAX
$(function () {
	$("#user").keyup(function () {
		validate_user();
	});
	$("#user").change(function () {
		validate_user();
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
	$("#email").change(function () {
		validate_email();
	});
});


// VARS
var _badEmail = false;
var _badUser = false;
var _badPass1 = false;
var _badPass2 = false;
var useremail;
var user;
var pass1;
var pass2;


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
function validate_email() {
	useremail_e = document.getElementById("email");
	useremail = useremail_e.value;
	email_label = document.getElementById("labele");

	const xhttp_prev_user = new XMLHttpRequest(); 
	xhttp_prev_user.open(
		"GET",
		"prev_user.php?email=" + useremail,
		false
	);
	xhttp_prev_user.send();
	_isNew = xhttp_prev_user.responseText;

	console.log(useremail + " is new: " + _isNew);
	if (_isNew == "false") {
		changeRed(useremail_e);
		changeRed(email_label);
		changeBold(email_label);
	}
	else if (_isNew == "true") {
		changeBlack(useremail_e);
		changeWhite(email_label);
		changeBack(email_label);
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
	if (_badEmail || _badUser || _badPass1 || _badPass2) {
		alert("Invalid email, username, or password");
	}
	else {
		const xhttp_register = new XMLHttpRequest(); 
		xhttp_register.open(
			"GET",
			"register.php?email=" + useremail + "&user=" + user.value,
			false
		);
		xhttp_register.setRequestHeader("Content-type", "text/html");
		xhttp_register.send();
		res = xhttp_register.response;
		document.querySelector("html").innerHTML = res;
		console.log("SUCCESSFULLLL");
	}
}