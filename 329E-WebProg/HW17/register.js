$(function () {
	$('#submitBtn').click(function () {
		submit();
	});
});

function submit() {
	// AJAX
	var user_e = document.getElementById("user");
	var userval = user_e.value;
	var pass_e = document.getElementById("pass");
	var passval = pass_e.value;

	const xhttp_submit = new XMLHttpRequest();
	xhttp_submit.open(
		"POST",
		"register.php",
		false
	);
	xhttp_submit.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp_submit.send("user=" + userval + "&pass=" + passval);

	response = xhttp_submit.responseText;

	switch (response) {
		case "confirm":
			alert("User and password confirmed");
			break;
		case "update":
			alert("Password changed");
			break;
		case "register":
			alert("New user registered");
			break;
		default:
			console.log(response);
			break;
	}
}