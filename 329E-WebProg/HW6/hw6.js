function calculate() {
	var P = parseFloat(document.getElementById("P").value);
	var I_Yr = parseFloat(document.getElementById("Yr").value);
	var n_months = parseInt(document.getElementById("n").value);

	if(P < 0.0 || I_Yr < 0.0 || n_months < 0.0){
		alert("Negative values are not allowed");
		return;
	}
	if(I_Yr > 1.0){
		alert(I_Yr+" is not an allowed value, as it is > 1.0");
		return;
	}

	var I_mo = I_Yr/12

	var R = (P * I_mo) / (1 - (1 / ( (1+I_mo) ** n_months ) ) )
	var Rt = R * n_months
	var It = Rt - P
	
	document.getElementById("R").value = R.toFixed(2);
	document.getElementById("Rt").value = Rt.toFixed(2);
	document.getElementById("It").value = It.toFixed(2);
}