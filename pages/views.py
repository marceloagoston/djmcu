from django.views.generic import TemplateView

# vista que me lleva al home y luego me permite moverme por las demas vistas
class HomePageView(TemplateView):
	template_name = 'home.html'