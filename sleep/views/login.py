from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sleep.models.util import phash
from sleep.models.user import User

@view_config(route_name='login', renderer='login.mako')
def login_view(request):
    # are they already logged in; if so, push them through
    if request.user:
        return HTTPFound(location=request.route_url('home'))
    
    # they submitted the form
    if 'login' in request.POST:
        login = request.POST.get('login')
        password = request.POST.get('password')
        
        # if it has a @ in it, it's an email address
        if '@' in login:
            v = request.DBSession.query(User).filter(User.password == phash(password)).filter(User.email == login)
        else:
            v = request.DBSession.query(User).filter(User.password == phash(password)).filter(User.username == login)
        
        # did they match?
        if v.count() == 1:
            request.session['user_id']  = v.one().id
            return HTTPFound(location=request.route_url('home'))
        
        # incorrect username/email/password
        request.session.flash('incorrect login/password combination')
        
    return {}