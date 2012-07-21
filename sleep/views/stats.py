from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sleep.models.sleep import Sleep
from sleep.models.stats import sleep_time_stats

@view_config(route_name='stats', renderer='stats.mako')
def stats_view(request):
    # get ALL the records
    rs = request.DBSession.query(Sleep).all()
    
    (avg_sleep_duration, ojs, start_stats, tts, end_stats, avg_sleep_quality) = sleep_time_stats(rs)
    
    return {'title' : 'global stats',
            'avg_sleep_duration' : avg_sleep_duration,
            'avg_sleep_quality' : avg_sleep_quality,
            's1_data' : ojs,
            's1_stats' : start_stats,
            's2_data' : tts,
            's2_stats' : end_stats}
            
@view_config(route_name='pstats', renderer='stats.mako')
def pstats_view(request):
    # we have to be logged in for this one
    if not request.user:
        return HTTPFound(location=request.route_url('home'))
        
    # get our users records
    rs = request.user.records
    
    (avg_sleep_duration, ojs, start_stats, tts, end_stats, avg_sleep_quality) = sleep_time_stats(rs)
    
    return {'title' : 'personal stats',
            'avg_sleep_duration' : avg_sleep_duration,
            'avg_sleep_quality' : avg_sleep_quality,
            's1_data' : ojs,
            's1_stats' : start_stats,
            's2_data' : tts,
            's2_stats' : end_stats}
            