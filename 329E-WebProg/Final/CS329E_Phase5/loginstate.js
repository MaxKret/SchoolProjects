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
        loggedin = false;
        username = "";
	}
	else {
        
		xhttp_seshmanager_loggedin_set.open(
			"GET",
			"seshmanager.php?op=set&key=loggedin&val=true",
			false
		);
		xhttp_seshmanager_loggedin_set.send();
        loggedin = true;
        username = cookieVal;
	}

    if(loggedin === true){
        $("#topright1").hide();
        $("#topright2 li p").text("Hello, " + username);
        $("#topright2").show();
    }
    else{
        $("#topright1").show();
        $("#topright2").hide();
    }

})

// VARS
var username = "";   //stores username
var loggedin = false;   //user logged in? true or false