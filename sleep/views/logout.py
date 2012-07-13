from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

@view_config(route_name='logout')
def logout_view(request):
    # LOG THEM OUT
    request.session['user_id'] = False
    request.user = False
    
    # now be gone
    return HTTPFound(location=request.route_url('home'))