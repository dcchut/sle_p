from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sleep.models.util import phash
from sleep.models.sleep import Sleep
from sleep.models.stats import sleep_time_stats
from sleep.models.user import User

def ulhash(user):
    return phash(user.password[-10:] + 'i love to eat crocodiles' + user.username + 'hello there' + user.id)[:10]

@view_config(route_name='stats', renderer='stats.mako')
def stats_view(request):
    # get ALL the records
    rs = request.DBSession.query(Sleep).all()
    
    (avg_sleep_duration, ojs, start_stats, tts, end_stats, avg_sleep_quality, sleep_duration_byday, sleep_quality_byday) = sleep_time_stats(rs)
    
    return {'title' : 'global stats',
            'avg_sleep_duration' : avg_sleep_duration,
            'avg_sleep_quality' : avg_sleep_quality,
            's1_data' : ojs,
            's1_stats' : start_stats,
            's2_data' : tts,
            's2_stats' : end_stats,
            'sd_byday' : sleep_duration_byday,
            'sq_byday' : sleep_quality_byday}
            
@view_config(route_name='pstats', renderer='stats.mako')
def pstats_view(request):
    # we have to be logged in for this one
    if not request.user:
        return HTTPFound(location=request.route_url('home'))
        
    # get our users records
    rs = request.user.records
    
    (avg_sleep_duration, ojs, start_stats, tts, end_stats, avg_sleep_quality, sleep_duration_byday, sleep_quality_byday) = sleep_time_stats(rs)
    
    return {'title' : 'personal stats',
            'avg_sleep_duration' : avg_sleep_duration,
            'avg_sleep_quality' : avg_sleep_quality,
            's1_data' : ojs,
            's1_stats' : start_stats,
            's2_data' : tts,
            's2_stats' : end_stats,
            'sd_byday' : sleep_duration_byday,
            'sq_byday' : sleep_quality_byday,
            'user_hash' : ulhash(request.user)}
            
@view_config(route_name='vstats', renderer='stats.mako')
def vstats_view(request):
    if 'username' not in request.matchdict or 'hash' not in request.matchdict:
        return HTTPFound(location=request.route_url('home'))

    # verify the username exists
    urs = request.DBSession.query(User).filter(User.username == request.matchdict['username']).all()
    
    # user does not exist
    if len(urs) != 1:
        return HTTPFound(location=request.route_url('home'))
    
    # otherwise we have the user record, now verify the hash
    user = urs[0]
    
    if request.matchdict['hash'] != ulhash(user):
        return HTTPFound(location=request.route_url('home'))
    
    # get the sleep stats
    (avg_sleep_duration, ojs, start_stats, tts, end_stats, avg_sleep_quality, sleep_duration_byday, sleep_quality_byday) = sleep_time_stats(user.records)
    
    return {'title' : user.username + '\'s personal stats',
            'avg_sleep_duration' : avg_sleep_duration,
            'avg_sleep_quality' : avg_sleep_quality,
            's1_data' : ojs,
            's1_stats' : start_stats,
            's2_data' : tts,
            's2_stats' : end_stats,
            'sd_byday' : sleep_duration_byday,
            'sq_byday' : sleep_quality_byday,}