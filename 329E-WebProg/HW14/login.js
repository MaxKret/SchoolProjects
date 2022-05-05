
function login() {
	var loginUser_e = document.getElementById("loginUser");
	var loginUserval = loginUser_e.value;
	var loginPass_e = document.getElementById("loginPass");
	var loginPassval = loginPass_e.value;
	let loginpage = "https://spring-2022.cs.utexas.edu/cs329e-bulko/maxkret/HW14/login.html";

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