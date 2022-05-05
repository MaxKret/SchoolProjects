// AJAX
$(function () {
	const xhttp_seshmanager_cookie_get = new XMLHttpRequest();
	xhttp_seshmanager_cookie_get.open(
		"GET",
		"seshmanager.php?op=get&key=cookie",
		false
	);
	xhttp_seshmanager_cookie_get.send();
	let cookieVal = xhttp_seshmanager_cookie_get.responseText;

	const xhttp_seshmanager_loggedin_set = new XMLHttpRequest();
	if (cookieVal === "false") {
		xhttp_seshmanager_loggedin_set.open(
			"GET",
			"seshmanager.php?op=set&key=loggedin&val=false",
			false
		);
		xhttp_seshmanager_loggedin_set.send();
	}
	else {
		xhttp_seshmanager_loggedin_set.open(
			"GET",
			"seshmanager.php?op=set&key=loggedin&val=true",
			false
		);
		xhttp_seshmanager_loggedin_set.send();
	}


	$('.logreq').click(function (event) {
		let loginpage = "https://spring-2022.cs.utexas.edu/cs329e-bulko/maxkret/HW14/login.html";
		event.preventDefault();
		reqfile = this.href;
		const xhttp_seshmanager_redir_set = new XMLHttpRequest();
		xhttp_seshmanager_redir_set.open(
			"GET",
			"seshmanager.php?op=set&key=redirect&val=" + reqfile,
			false
		);
		xhttp_seshmanager_redir_set.send();

		const xhttp_seshmanager_loggedin_get = new XMLHttpRequest();
		xhttp_seshmanager_loggedin_get.open(
			"GET",
			"seshmanager.php?op=get&key=loggedin",
			false
		);
		xhttp_seshmanager_loggedin_get.send();
		_isLoggedIn = xhttp_seshmanager_loggedin_get.responseText;

		if (_isLoggedIn === "false") {
			if (reqfile !== loginpage) {
				alert("You need an account to access this page, please log in or register");
			}
			window.location.href = "https://spring-2022.cs.utexas.edu/cs329e-bulko/maxkret/HW14/login.html";
		}
		else if (_isLoggedIn === "true") {
			window.location.href = reqfile;
		}
		else {
			console.log("failed redirect");
		}
	});
});