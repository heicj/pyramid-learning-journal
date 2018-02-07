from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def list_view(request):
	pass

def detail_view(request):
	pass
	
def create_view(request):
	pass
	
def update_view(request):
	pass

	
if __name__ == '__main__':
	config.add_route('home','/')
	config.add_view(list_view, route_name = 'home')

	config.add_route('detail_view', '/journal/{id:\d+}')
	config.add_view(detail_view, route_name = 'detail_view')

	config.add_route('create_view', '/journal/new-entry')
	config.add_view(create_view, route_name = 'create_view')

	config.add_route('update_view', '/journal/{id:\d+}/edit-entry')
	config.add_view(update_view, route_name = 'update_view')
	
	app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 6543, app)  		#0.0.0.0 is same as 127.0.0.1 in some cases such as this, 6543 is port
	server.serve_forever()
