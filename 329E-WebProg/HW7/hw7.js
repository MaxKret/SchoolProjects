// AJAX
$(function () {
	$("#user").keyup(function () {
		validate_user();
	})
	$("#user").change(function () {
		validate_user();
	})
	$("#pass1").keyup(function () {
		validate_password1();
	})
	$("#pass1").change(function () {
		validate_password1();
	})
	$("#pass2").keyup(function () {
		validate_password2();
	})
	$("#pass2").change(function () {
		validate_password2();
	})
})

// HELPER METHODS
function changeRed(target) {
	target.style.color = "red";
}
function changeBlack(target) {
	target.style.color = "black";
}
function changeBold(target) {
	target.style.fontWeight = "bold";
}
function changeBack(target) {
	target.style.fontWeight = 'normal';
}

// VALIDATION
function validate_password1() {
	// VARS
	regex_alphanum = /^[A-Za-z0-9][a-zA-Z0-9]{5,9}$/;
	regex_atleast = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,10}$/;
	pass1 = document.getElementById("pass1");
	pass1_label = document.getElementById("labelp1");

	if (!(pass1.value.match(regex_alphanum) && pass1.value.match(regex_atleast))) {
		changeRed(pass1);
		changeBold(pass1_label);
		console.log(pass1.value + " is not valid");
		return false;
	}
	else {
		changeBlack(pass1);
		changeBack(pass1_label);
		console.log(pass1.value + " is valid");
		return true;
	}
}

function validate_password2() {
	pass2 = document.getElementById("pass2");
	pass2_label = document.getElementById("labelp2");

	if (pass1.value != pass2.value) {
		changeRed(pass2);
		changeBold(pass2_label);
		console.log(pass2.value + " does not match");
		return false;
	}
	else {
		changeBlack(pass2);
		changeBack(pass2_label);
		console.log(pass2.value + " matches");
		return true;
	}
}

function validate_user() {

	regex_alphanum_user = /^[A-Za-z][a-zA-Z0-9]{5,9}$/;
	user = document.getElementById("user");
	user_label = document.getElementById("labelu");

	if (!(user.value.match(regex_alphanum_user))) {
		changeRed(user);
		changeBold(user_label);
		console.log(user.value + " is not valid");
		return false;
	}
	else {
		changeBlack(user);
		changeBack(user_label);
		console.log(user.value + " is valid");
		return true;
	}
}

function validate() {
	if (validate_user() && validate_password1() && validate_password2()) {
		alert("User validated");
	}
	else {
		alert("Invalid username or password");
	}
}