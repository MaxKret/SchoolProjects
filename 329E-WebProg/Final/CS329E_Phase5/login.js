
function login() {
	var loginUser_e = document.getElementById("loginUser");
	var loginUserval = loginUser_e.value;
	var loginPass_e = document.getElementById("loginPass");
	var loginPassval = loginPass_e.value;

	const xhttp_prev_user = new XMLHttpRequest();
	xhttp_prev_user.open(
		"GET",
		"login.php?loginUser=" + loginUserval + "&loginPass=" + loginPassval,
		false
	);
	xhttp_prev_user.send();
	_isAccount = xhttp_prev_user.responseText;

	const xhttp_seshmanager_loggedin_set = new XMLHttpRequest();
	if (_isAccount === "true") {
		const xhttp_seshmanager_cookie_set = new XMLHttpRequest();
		xhttp_seshmanager_cookie_set.open(
			"GET",
			"seshmanager.php?op=set&key=cookie&val=" + loginUserval,
			false
		);
		xhttp_seshmanager_cookie_set.send();

		xhttp_seshmanager_loggedin_set.open(
			"GET",
			"seshmanager.php?op=set&key=loggedin&val=true",
			false
		);
		xhttp_seshmanager_loggedin_set.send();

	}
	else {
		xhttp_seshmanager_loggedin_set.open(
			"GET",
			"seshmanager.php?op=set&key=redirect&val=false",
			false
		);
		xhttp_seshmanager_loggedin_set.send();
		alert("No account exists or incorrect password")
	}
}