from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

import io
import os

HERE = os.path.dirname(__file__)

def list_view(request):
	imported_text = io.open(os.path.join(HERE, '../templates/index.html')).read()
	return Response(imported_text)

def detail_view(request):
	imported_text = io.open(os.path.join(HERE, '../templates/detail.html')).read()
	return Response(imported_text)
	
def create_view(request):
	imported_text = io.open(os.path.join(HERE, '../templates/new.html')).read()
	return Response(imported_text)
	
def update_view(request):
	imported_text = io.open(os.path.join(HERE, '../templates/edit.html')).read()
	return Response(imported_text)
	
def includeme(config):
	#config.add_static_view('../static/style.css', '', cache_max_age=3600)
	pass
	
	
if __name__ == '__main__':
	config = Configurator()
	config.add_route('home','/index.html')
	config.add_view(list_view, route_name = 'home')
	
	config.add_route('detail_view', '/detail.html')
	config.add_view(detail_view, route_name = 'detail_view')
	
	config.add_route('create_view', '/new.html')
	config.add_view(create_view, route_name = 'create_view')
	
	config.add_route('update_view', '/edit.html')
	config.add_view(update_view, route_name = 'update_view')
	
	
	app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 6543, app)  		#0.0.0.0 is same as 127.0.0.1 in some cases such as this, 6543 is port
	server.serve_forever()
