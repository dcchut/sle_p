from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sleep.models.sleep import Sleep

@view_config(route_name='delete')
def delete_view(request):
    # if they aren't logged in, throw them out
    if not request.user:
        return HTTPFound(location=request.route_url('home'))
    
    # if they haven't put in an id, throw them out
    if 'id' not in request.matchdict or not request.matchdict['id'].isdigit():
        return HTTPFound(location=request.route_url('home'))
    
    # is this sleep record in this users records?
    record = request.DBSession.query(Sleep).with_parent(request.user).filter(Sleep.id==request.matchdict['id'])
    
    if record.count():
        request.DBSession.delete(record.first())
        request.session.flash('record successfully deleted')
    else:
        request.session.flash('go away')
    
    return HTTPFound(location=request.route_url('home'))