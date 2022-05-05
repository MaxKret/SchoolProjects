
function login() {
	// AJAX
	var loginUser_e = document.getElementById("loginUser");
	var loginUserval = loginUser_e.value;
	var loginPass_e = document.getElementById("loginPass");
	var loginPassval = loginPass_e.value;

	const xhttp_login = new XMLHttpRequest();
	xhttp_login.open(
		"GET",
		"login.php?loginUser=" + loginUserval + "&loginPass=" + loginPassval,
		false
	);
	xhttp_login.send();

	_isAccount = xhttp_login.responseText;

	if (_isAccount === "true") {
		alert("Success!")
		window.location.href = "https://spring-2022.cs.utexas.edu/cs329e-bulko/maxkret/HW16/actions.php";
	}
	else {
		alert("You are not authorized");
		window.location.href = "https://spring-2022.cs.utexas.edu/cs329e-bulko/maxkret/HW16/login.html";
	}
}