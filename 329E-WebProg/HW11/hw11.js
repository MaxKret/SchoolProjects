// AJAX
$(function () {
	shuffleLoad();
	computeGridCenters();
	startTimer();
	$('#submit').click(function () {
		console.log("submit");
		checkSolution();
	});
	$('#reset').click(function () {
		console.log("reset");
		stopTimer();
		document.getElementById('timeElapsed').innerText = 0;
		shuffleLoad();
		startTimer();
	});
	$(window).resize(function () {
		computeGridCenters();
	});
});


// VARS
// 	[top,left]
var loadPos = [[450, 200], [450, 350], [450, 500], [450, 650], [600, 200], [600, 350], [600, 500], [600, 650], [750, 200], [750, 350], [750, 500], [750, 650]];
var gridTopLeft = [0, 0];
var gridTops = [];
var gridCenters = [];
var timerId;
var secElapsed = 0;


function checkSolution() {
	let imgs = document.querySelectorAll('img[class="dragImg"]');
	let resultText = document.getElementById('resultText');
	let imglocs = [];
	for (const img of imgs) {
		imglocs.push([parseInt(img.style.left), parseInt(img.style.top)]);
	}
	if (arraysEqual(imglocs,gridTops)) {
		stopTimer();
		resultText.innerText = "Congratulations! You got it!";
	}
	else {
		resultText.innerText = "Better luck next time! Try again or click Reset";
	}
}

function arraysEqual(a1, a2) {
	if (a1.length != a2.length) {
		return false;
	}
	for (let i = 0; i < a1.length; i++) {
		if ((a1[i][0] != a2[i][0]) || (a1[i][1] != a2[i][1])) {
			return false;
		}
	}
	return true;
}


function startTimer() {
	secElapsed = 0;
	timerId = setInterval(() => {
		secElapsed += 1;
		document.getElementById('timeElapsed').innerText = secElapsed;
	}, 1000);
}
function stopTimer() {
	clearInterval(timerId);
}


function shuffleLoad() {
	// Pick Puzzle
	puzzle_idx = Math.floor(Math.random() * 3);
	setSources(puzzle_idx);
	setInitPos();
}

function setSources(puzzle_idx) {
	let imgs = document.querySelectorAll('img[class="dragImg"]');
	for (let i = 0; i < 12; i++) {
		imgs[i].src = "puzzle" + (puzzle_idx + 1) + "/img" + (puzzle_idx + 1) + "-" + (i + 1) + ".jpg";
	}
}

function setInitPos() {
	let idxs = shuffleIdx();
	for (let i = 0; i < 12; i++) {
		let e = document.getElementById("img" + (idxs[i]));
		e.style.top = loadPos[i][0] + "px";
		e.style.left = loadPos[i][1] + "px";
	}
}

function shuffleIdx() {
	let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
	for (let i = array.length - 1; i > 0; i--) {
		let j = Math.floor(Math.random() * (i + 1));
		[array[i], array[j]] = [array[j], array[i]];
	}
	return array;
}


function grabber(event) {
	// Set the global variable for the element to be moved
	theElement = event.currentTarget;

	// Determine the position of the word to be grabbed, first removing the units from left and top
	init_posX = parseInt(theElement.style.left);
	init_posY = parseInt(theElement.style.top);

	// Compute the difference between where it is and where the mouse click occurred
	diffX = event.clientX - init_posX;
	diffY = event.clientY - init_posY;

	// Now register the event handlers for moving and dropping the word
	document.addEventListener("mousemove", mover, true);
	document.addEventListener("mouseup", dropper, true);
}

function mover(event) {
	// Compute the new position, add the units, and move the word
	theElement.style.left = (event.clientX - diffX) + "px";
	theElement.style.top = (event.clientY - diffY) + "px";
}

function dropper(event) {
	// Unregister the event handlers for mouseup and mousemove
	document.removeEventListener("mouseup", dropper, true);
	document.removeEventListener("mousemove", mover, true);
	// Find nearest grid cell to drop
	dropClosest();
}

function dropClosest() {
	let eCenterX = parseInt(theElement.style.left) + 50;
	let eCenterY = parseInt(theElement.style.top) + 50;
	let minDistanceKey = getMinDistance(eCenterX, eCenterY, gridCenters);
	if (minDistanceKey == "None") { console.log("None"); return; }
	let closestCellCenterPos = gridCenters[parseInt(minDistanceKey) - 1];
	let closestCellX = closestCellCenterPos[0] - 50;
	let closestCellY = closestCellCenterPos[1] - 50;
	theElement.style.left = closestCellX + "px";
	theElement.style.top = closestCellY + "px";
}

function getMinDistance(fromX, fromY, toArray) {
	let dists = [];
	let distsdict = {};
	for (const coord of toArray) {
		let dist = Math.sqrt((coord[0] - fromX) ** 2 + (coord[1] - fromY) ** 2);
		dists.push(dist);
	}
	for (let i = 0; i < 12; i++) {
		distsdict[i + 1] = dists[i];
	}
	let minkey = Object.keys(distsdict).reduce((key, v) => distsdict[v] < distsdict[key] ? v : key);
	let minval = distsdict[minkey];
	return (minval < 100 ? minkey : "None");
}

function computeGridCenters() {
	let grid = document.querySelector('img.backImg');
	gridTopLeft[0] = grid.x;
	gridTopLeft[1] = grid.y;

	let currTopLeftX = gridTopLeft[0];
	let currX = gridTopLeft[0];
	let currY = gridTopLeft[1];

	for (let i = 0; i < 3; i++) {
		for (let i = 0; i < 4; i++) {
			gridTops.push([currX, currY]);
			currX += 100;
		}
		currX = currTopLeftX;
		currY += 100;
	}
	for (const coord of gridTops) {
		gridCenters.push([coord[0] + 50, coord[1] + 50]);
	}
}