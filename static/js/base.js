function login(){
	let lad = document.getElementById('nav');
	const wide = matchMedia('(max-width: 800px)');
	
	// console.log(wide);
	// console.log(wide.matches);

	function chsz(){
		

		if (wide.matches){
			lad.innerHTML=
			`
			<div class="dropdown dropleft rsp">
				  <button class="btn btn-secondary " type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fas fa-bars icono"></i>
				  </button>
				  <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
				    {% if user.is_authenticated %}
						<a href="{% url 'lista_activos' %}">Activos</a>
						  	<a href="{% url 'logout' %}"><i class="far fa-user"></i> {{user.username}}</a>
						    <a href="{% url 'logout' %}"><i class="fas fa-sign-out-alt"></i> Cerrar Sesión</a>
					{% else %}
						<a href="{% url 'login' %}"><i class="fas fa-sign-out-alt"></i> Iniciar Sesión</a>
					{% endif %}
				  </div>
			</div>
			`
		} else {
			lad.innerHTML=
			`
			<div class="nave">
					<a href="{% url 'home' %}">Inicio</a>
					{% if user.is_authenticated %}
						<a href="{% url 'lista_activos' %}">Activos</a>
						<div class="dropdown">	
						  	<button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
						    <i class="far fa-user"></i> {{user.username}}
						  	</button>
						  	<div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
						    	<a href="{% url 'logout' %}"><i class="fas fa-sign-out-alt"></i> Cerrar Sesión</a>
						  	</div>
						</div>
					{% else %}
						<a href="{% url 'login' %}"><i class="fas fa-sign-out-alt"></i> Iniciar Sesión</a>
					{% endif %}
			</div>

			`
		}

	};
wide.addListener(chsz);
chsz(wide);
}


