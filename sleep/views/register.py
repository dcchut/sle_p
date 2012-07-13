from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from sleep.models.user import User
from sleep.models.util import phash
from sqlalchemy import or_
import time

@view_config(route_name='register', renderer='register.mako')
def register_view(request):
    # what are you doing here?
    if request.user:
        return HTTPFound(location=request.route_url('home'))
    
    # keep track of some of the register fields in case they screw up
    vv = {'username' : '', 'email' : ''}
    
    if 'username' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')
        
        if username:
            vv['username'] = username
            
        if email:
            vv['email'] = email
            
        
        v = True
        
        if not username or not password or not cpassword or not email:
            request.session.flash('please ensure all fields are filled in')
        else:
            # verify username    
            if not username.isalnum():
                v = False
                request.session.flash('your username must be alphanumeric')
                
            if len(username) > 20:
                v = False
                request.session.flash('your username can be at most 20 characters long')
                
            # verify passwords
            if password != cpassword:
                v = False
                request.session.flash('your passwords dont match')
            
            # verify email address
            if '@' not in email or len(email) > 128:
                v = False
                request.session.flash('your email address is invalid') 
                
            # did we win?
            if v:
                # is there already a user with this username/email?
                q = request.DBSession.query(User).filter(or_(User.username == username, User.email == email))
                
                if q.count() != 0:
                #u = user.new(request, username, password, email)
                #
                #if not u:
                    request.session.flash('your username/email address is already in use')
                else:
                    u = User(username=username,
                             password=phash(password),
                             email=email,
                             joindate=int(time.time()))
                    request.DBSession.add(u)
                    
                    # now we have to get the user
                    request.session['user_id'] = request.DBSession.query(User).filter(User.username == username).one().id
                    
                    # redirect to glory
                    request.session.flash('you have successfully registered')
                    
                    return HTTPFound(location=request.route_url('home'))

    return vv