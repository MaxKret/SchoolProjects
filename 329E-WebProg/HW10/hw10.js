function calculate() {
	var q1 = document.querySelectorAll('input[name="q1a"]:checked');
	if (q1.length !== 1) { alert("Please answer all questions"); return; }
	var q1a = q1[0].value;

	var q2 = document.querySelectorAll('input[name="q2a"]:checked');
	if (q2.length !== 1) { alert("Please answer all questions"); return; }
	var q2a = q2[0].value;

	var q3 = document.querySelectorAll('input[name="q3a[]"]:checked');
	if (q3.length < 1) { alert("Please answer all questions"); return; }
	var q3a = [];

	var q4 = document.querySelectorAll('input[name="q4a[]"]:checked');
	if (q4.length < 1) { alert("Please answer all questions"); return; }
	var q4a = [];

	var q5a = document.getElementById("q5a").value.toLowerCase();
	if (q5a.length < 1) { alert("Please answer all questions"); return; }

	var q6a = document.getElementById("q6a").value.toLowerCase();
	if (q6a.length < 1) { alert("Please answer all questions"); return; }

	for (const e of q3) {
		if (e.checked) {
			q3a.push(e.value);
		}
	}
	if (q3a.length > 1) { q3a = 'false'; }
	else { q3a = q3a[0]; }

	for (const e of q4) {
		if (e.checked) {
			q4a.push(e.value);
		}
	}
	if (q4a.length > 1) { q4a = 'false'; }
	else { q4a = q4a[0]; }

	// Answer Checking

	// Create an XMLHttpRequest object
	const xhttp = new XMLHttpRequest();

	// // Define a callback function
	// xhttp.onload = function() {
		
	// }

	// Send a request  
	xhttp.open(
		"GET",
		"hw10.php?q1=" + q1a + "&q2=" + q2a + "&q3=" + q3a +
		"&q4=" + q4a + "&q5=" + q5a + "&q6=" + q6a,
		false
	);
	xhttp.send();

	score = xhttp.responseText;
	alert("Your grade is " + score + " / 6.");
}