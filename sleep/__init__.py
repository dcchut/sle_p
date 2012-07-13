from pyramid_beaker import session_factory_from_settings
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from sleep.models.models import DBSession
from sleep.models.user import User

from pyramid.events import NewRequest, subscriber

# we want some session defaults
@subscriber(NewRequest)
def new_request_subscriber(event):
    request = event.request
    
    if 'user_id' not in request.session or not request.session['user_id']:
        request.session['user_id'] = False
        request.user = False
    else:
        # verify their user record is "still" good
        try:
            request.user = DBSession.query(User).filter(User.id==request.session['user_id']).one()
        except (MultipleResultsFound, NoResultFound) as e:
            request.session['user_id'] = False
            request.user = False
        
    request.DBSession = DBSession
        
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)

    # magical routing!
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('register', '/register')
    config.add_route('logout', '/logout')
    config.add_route('delete', '/delete/{id}')
    config.add_route('stats', '/stats')
    config.add_route('pstats', '/pstats')
    
    session_factory = session_factory_from_settings(settings)
    config.set_session_factory(session_factory)
    
    config.scan()
    return config.make_wsgi_app()

