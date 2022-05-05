// AJAX
$(function () {
	$('.cellBtns').click(function () {
		clicked(this);
	});
	$('#reset').click(function () {
		resetGame();
	});
	currPlayer = 'X';
	document.getElementById('currPlayer').innerText = currPlayer;
});

// VARS
var emptyCell = '&nbsp;&nbsp;&nbsp;';
var scoreX = 0;
var scoreO = 0;
var currPlayer = 'X';


// FUNCS
function nextPlayer() {
	currPlayer = ((currPlayer == 'X') ? 'O' : 'X');
	document.getElementById('currPlayer').innerText = currPlayer;
}

function clicked(element) {
	if (element.innerHTML == emptyCell) {
		element.innerText = currPlayer;

		if (checkWin()) {
			if (currPlayer == 'X') { scoreX += 1; }
			else { scoreO += 1; }

			document.getElementById('scoreX').innerText = scoreX;
			document.getElementById('scoreO').innerText = scoreO;

			alert(currPlayer + " has Won");
		}
		else { nextPlayer(); return; }
	}
	else { return; }
}

function checkWin() {
	// VARS
	let c1 = '';
	let c2 = '';
	let c3 = '';
	let grid = [];
	for (const btn of document.querySelectorAll('.cellBtns')) { grid.push(btn.innerHTML); }

	// ROWS
	if ( (grid[0] != '&nbsp;&nbsp;&nbsp;') && (grid[0] == grid[1]) && (grid[1] == grid[2]) ) {
		return true;
	}
	if ( (grid[3] != '&nbsp;&nbsp;&nbsp;') && (grid[3] == grid[4]) && (grid[4] == grid[5]) ) {
		return true;
	}
	if ( (grid[6] != '&nbsp;&nbsp;&nbsp;') && (grid[6] == grid[7]) && (grid[7] == grid[8]) ) {
		return true;
	}
	
	// COLS
	if ( (grid[0] != '&nbsp;&nbsp;&nbsp;') && (grid[0] == grid[3]) && (grid[3] == grid[6]) ) {
		return true;
	}
	if ( (grid[1] != '&nbsp;&nbsp;&nbsp;') && (grid[1] == grid[4]) && (grid[4] == grid[7]) ) {
		return true;
	}
	if ( (grid[2] != '&nbsp;&nbsp;&nbsp;') && (grid[2] == grid[5]) && (grid[5] == grid[8]) ) {
		return true;
	}
	
	// DIAG
	if ( (grid[8] != '&nbsp;&nbsp;&nbsp;') && (grid[0] == grid[4]) && (grid[4] == grid[8]) ) {
		return true;
	}
	if ( (grid[4] != '&nbsp;&nbsp;&nbsp;') && (grid[2] == grid[4]) && (grid[4] == grid[6]) ) {
		return true;
	}

	return false;
}

function resetGame() {
	currPlayer = 'X';
	document.getElementById('currPlayer').innerText = currPlayer;
	for (const btn of document.querySelectorAll('.cellBtns')) {
		btn.innerHTML = emptyCell;
	}
}