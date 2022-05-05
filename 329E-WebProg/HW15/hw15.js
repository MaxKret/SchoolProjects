// AJAX
$(function () {
	startTimer();
	showQuestion();
});

// GLOBAL VARS
var q_idx = 0;
var submit_ans;

// FUNCS
function startTimer() {
	timerId = setTimeout(() => {
		endTimer();
	}, 900000);
}

function endTimer() {
	clearInterval(timerId);
	const xhttp_clear_session = new XMLHttpRequest();
	xhttp_clear_session.open(
		"GET",
		"seshmanager.php?loginUser=" + loginUserval + "&op=clear",
		false
	);
	xhttp_clear_session.send();
	window.location.href = "https://spring-2022.cs.utexas.edu/cs329e-bulko/maxkret/HW15/login.html"
}

function nextQuestion() {
	q_idx += 1;
	showQuestion();
}

function showQuestion() {
	let current_q;
	let current_q_label;
	let last_q;
	let last_q_label;

	switch (q_idx) {
		case 0:
			current_q = document.getElementById("Q1");
			current_q_label = document.getElementById("labelS1");

			current_q.style.display = "block";
			current_q_label.style.display = "block";

			break;

		case 1:
			current_q = document.getElementById("Q2");
			current_q_label = document.getElementById("labelS1");
			last_q = document.getElementById("Q1");

			last_q.style.display = "none";

			current_q.style.display = "block";
			current_q_label.style.display = "block";

			break;

		case 2:
			current_q = document.getElementById("Q3");
			current_q_label = document.getElementById("labelS2");
			last_q = document.getElementById("Q2");
			last_q_label = document.getElementById("labelS1");

			last_q.style.display = "none";
			last_q_label.style.display = "none";

			current_q.style.display = "block";
			current_q_label.style.display = "block";

			break;

		case 3:
			current_q = document.getElementById("Q4");
			current_q_label = document.getElementById("labelS2");
			last_q = document.getElementById("Q3");

			last_q.style.display = "none";

			current_q.style.display = "block";
			current_q_label.style.display = "block";

			break;

		case 4:
			current_q = document.getElementById("Q5");
			current_q_label = document.getElementById("labelS3");
			last_q = document.getElementById("Q4");
			last_q_label = document.getElementById("labelS2");

			last_q.style.display = "none";
			last_q_label.style.display = "none";

			current_q.style.display = "block";
			current_q_label.style.display = "block";

			break;

		case 5:
			current_q = document.getElementById("Q6");
			current_q_label = document.getElementById("labelS3");
			last_q = document.getElementById("Q5");

			last_q.style.display = "none";

			current_q.style.display = "block";
			current_q_label.style.display = "block";

			break;

	}
}

function submitAns() {
	switch (q_idx) {
		case 0:
			let q1 = document.querySelectorAll('input[name="q1a"]:checked');
			if (q1.length !== 1) { alert("Please answer the question"); return; }
			submit_ans = q1[0].value;

			break;

		case 1:
			let q2 = document.querySelectorAll('input[name="q2a"]:checked');
			if (q2.length !== 1) { alert("Please answer the question"); return; }
			submit_ans = q2[0].value;

			break;

		case 2:
			let q3 = document.querySelectorAll('input[name="q3a[]"]:checked');
			if (q3.length < 1) { alert("Please answer the question"); return; }
			submit_ans = [];
			for (const e of q3) {
				if (e.checked) {
					submit_ans.push(e.value);
				}
			}
			if (submit_ans.length > 1) { submit_ans = 'false'; }
			else { submit_ans = submit_ans[0]; }

			break;

		case 3:
			let q4 = document.querySelectorAll('input[name="q4a[]"]:checked');
			if (q4.length < 1) { alert("Please answer the question"); return; }
			submit_ans = [];
			for (const e of q4) {
				if (e.checked) {
					submit_ans.push(e.value);
				}
			}
			if (submit_ans.length > 1) { submit_ans = 'false'; }
			else { submit_ans = submit_ans[0]; }

			break;

		case 4:
			submit_ans = document.getElementById("q5a").value.toLowerCase();
			if (submit_ans.length < 1) { alert("Please answer the question"); return; }

			break;

		case 5:
			submit_ans = document.getElementById("q6a").value.toLowerCase();
			if (submit_ans.length < 1) { alert("Please answer the question"); return; }

			break;
	}

	const xhttp_submit_ans = new XMLHttpRequest();
	xhttp_submit_ans.open(
		"GET",
		"hw15.php?ans=" + submit_ans + "&idx=" + q_idx,
		false
	);
	xhttp_submit_ans.send();

	res = xhttp_submit_ans.responseText;

	if (parseInt(res)) {
		alert("Your score is " + parseInt(res) + "/60");
	}
	else {
		nextQuestion();
	}

}