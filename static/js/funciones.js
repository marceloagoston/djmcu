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

function mostrarListaAmenazas(){
	let ag_bot = document.getElementById("ag-bot");
  	let ag_tab = document.getElementById("ag-tab");
    cond = false;    
    ag_bot.onclick = () => {
    	if (cond==true){
        	ag_tab.style.display = "none";
            ag_bot.innerHTML = `<i class="far fa-eye"></i> Mostrar Lista de Amenazas`
            cond = false;
            } else{
            	ag_tab.style.display = "block";
                ag_bot.innerHTML = `<i class="far fa-eye-slash"></i> Ocultar Lista Amenazas`
                cond = true;
                }
            }
}
