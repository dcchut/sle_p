from pyramid.view import view_config
from sleep.models.sleep import Sleep

from collections import Counter
import numpy


@view_config(route_name='stats', renderer='stats.mako')
def stats_view(request):
    # get ALL the records
    rs = request.DBSession.query(Sleep).all()
    
    # average sleep duration?
    durations = [x.duration() for x in rs]

    avg_sleep_duration = sum(durations)/len(durations)
    avg_sleep_duration = round(avg_sleep_duration/float(60*60),2)
    
    # start sleep times
    start = [int(x.start.split(',')[0]) for x in rs]
    
    start_mcalc = []
    for i in start:
        if i <= 12:
            start_mcalc.append(i+24)
        else:
            start_mcalc.append(i)
    
    
    shc = Counter(start)
    start_stats = [numpy.mean(start_mcalc)-12, numpy.std(start_mcalc),max(shc.values())]
    
    ojs = '['
    j = 0
    for i in range(13,24) + range(0,13):
        if shc[i] != 0:
            ojs += '[' + str(j) + ',' + str(shc[i]) + '],'
        j += 1
    ojs = ojs[:-1] + ']'
    
    # wakeup times
    end = [int(x.end.split(',')[0]) for x in rs]
    shc = Counter(end)
    end_stats = [numpy.mean(end),numpy.std(end),max(shc.values())]
    
    tts = '['
    for i in range(0,24):
        if shc[i] == 0:
            continue
        tts += '[' + str(i) + ',' + str(shc[i]) + '],'
    tts = tts[:-1] + ']'
    
    return {'avg_sleep_duration' : avg_sleep_duration,
            's1_data' : ojs,
            's1_stats' : start_stats,
            's2_data' : tts,
            's2_stats' : end_stats}