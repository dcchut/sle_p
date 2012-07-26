from collections import Counter
import numpy

# computes sleep time stats for a given recordset
# in a format compatible with flot
def sleep_time_stats(rs):
    # average sleep duration?
    durations = [x.duration() for x in rs]

    avg_sleep_duration = sum(durations)/len(durations)
    avg_sleep_duration = round(avg_sleep_duration/float(60*60),2)
    
    # average sleep quality
    qualities = [x.quality for x in rs]
    avg_sleep_quality = round(sum(qualities)/float(len(qualities)),2)

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
    
    # sleep duration by day of week
    sd_step1 = [(x.ddate().weekday(),x.duration()) for x in rs]
    sd_step2 = [[x[1] for x in sd_step1 if x[0] == y] for y in range(0,7)]
    sd_step3 = [round((sum(x)/len(x))/float(60*60),2) for x in sd_step2]
    
    
    return (avg_sleep_duration, ojs, start_stats, tts, end_stats, avg_sleep_quality, sd_step3)