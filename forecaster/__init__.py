from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('forecast', '/api_v1')
    _add_static_views(config)
    config.scan()
    return config.make_wsgi_app()


def _add_static_views(config):
    config.add_static_view(name='fonts', path='static/fonts')
    config.add_static_view(name='css', path='static/css')
    config.add_static_view(name='js', path='static/js')
