// AJAX
$(function () {
	$('.cellBtns').click(function () {
		revealTile(this);
		$('#triesCt').text(tries);
		if (!matchFound) {
			$('#' + this.id).fadeOut({
				duration: 3000,
				easing: "swing",
				progress: function () {
					if (matchFound) {
						for (const i of matchPair) {
							$('#cellBtn' + i).stop();
							$('#cellBtn' + i).fadeIn(0);
						}
					}
				},
				complete: function () {
					if (!matchFound) {
						clearTile(this);
					}
					$('#' + this.id).fadeIn(0);
				}
			});
		}
	});
});

// VARS
var charsStr = "AABBCC112233";
var charsSplit = charsStr.split("");
var charsArr = getRandChars(charsSplit);

var clickedID1 = 0;
var clickedID2 = 0;
var currNumClicked = 0;
var revealed = [];
var emptyCell = '&nbsp;&nbsp;&nbsp;';
var matchFound = false;
var matchPair = [];
var tries = 0;


// FUNCS
function getRandChars(array) {
	for (let i = array.length - 1; i > 0; i--) {
		let j = Math.floor(Math.random() * (i + 1));
		[array[i], array[j]] = [array[j], array[i]];
	}
	return array;
}


function revealTile(element) {
	if ((element.innerHTML == emptyCell) && (currNumClicked <= 1)) {
		var clickedID = element.id.match(/\d+/)[0];
		var clickedElement = charsArr[clickedID - 1];
		matchFound = false;
		matchPair = [];

		element.innerText = clickedElement;
		revealed.push(clickedElement);
		currNumClicked += 1;

		switch (currNumClicked) {
			case 1:
				clickedID1 = clickedID;
				tries += 1;
				break;
			case 2:
				clickedID2 = clickedID;
				break;
		}

		// IF TWO REVEALED
		if ((currNumClicked > 1) && (revealed.length > 1)) {
			// MATCH FOUND
			if (revealed[0] == revealed[1]) {
				matchFound = true;
				matchPair.push(clickedID1);
				matchPair.push(clickedID2);
				revealed = [];
				currNumClicked = 0;
				clickedID1 = 0;
				clickedID2 = 0;
				// WIN CONDITION
				let allTiles = [];
				for (const e of document.querySelectorAll('.cellBtns')) { allTiles.push(e.innerHTML); }
				if ((allTiles.indexOf(emptyCell)) == -1) {
					alert('You succeeded with ' + tries + ' tries!');
				}
			}
			else { matchFound = false; }
		}
		else { return; }
	}
	else { return; }
}

function clearTile(e) {
	// clear revealed
	if (revealed.length < 2) {
		revealed.pop();
		clickedID1 = 0;
		clickedID2 = 0;
	}
	else {
		let idx = revealed.indexOf(e.innerText);
		if (idx == -1) { console.log("element not in revealed array"); }
		else {
			switch (idx) {
				case 0:
					revealed.unshift();
				case 1:
					revealed.pop();

			}
		}
	}
	// clear clickedId
	let tileID = e.id.match(/\d+/)[0];
	if (tileID === clickedID1) { clickedID1 = 0; }
	else { clickedID2 = 0; }

	currNumClicked -= 1;
	e.innerHTML = emptyCell;
}