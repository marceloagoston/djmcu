function valorRiesgo(){
	let riesgo = document.getElementsByClassName('riesgo');
		for (var i = 0; i < riesgo.length; i++) {
		    if (riesgo[i].innerText==1 || riesgo[i].innerText==2){
		    	riesgo[i].style.background = "lightgreen";
		    } else if (riesgo[i].innerText==3 || riesgo[i].innerText==4|| riesgo[i].innerText==6){
		    	riesgo[i].style.background = "lightgoldenrodyellow";
		    } else {
		    	riesgo[i].style.background = "lightcoral";
		    }
			}
}
// Esto se podria re factorizar
function valorPrioridad(){
	let valor = document.getElementsByClassName('ac_valor');
		for (var i = 0; i < valor.length; i++) {
		    if (valor[i].innerText==1){
		    	valor[i].style.background = "lightgreen";
		    } else if (valor[i].innerText==2){
		    	valor[i].style.background = "lightgoldenrodyellow";
		    } else {
		    	valor[i].style.background = "lightcoral";
		    }
			}
}