
function login() {
	// PHP
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

	_isNew = xhttp_login.responseText;

	if (_isNew === "true") {
		const xhttp_set_session = new XMLHttpRequest();
		xhttp_set_session.open(
			"GET",
			"seshmanager.php?loginUser=" + loginUserval + "&op=set",
			false
		);
		xhttp_set_session.send();
		alert("Success! Your 15min begins now")
		window.location.href = "https://spring-2022.cs.utexas.edu/cs329e-bulko/maxkret/HW15/hw15.html";
	}
	else {
		alert("This account has already taken this Quiz");
	}
}