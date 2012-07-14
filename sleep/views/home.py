from pyramid.view import view_config
from sleep.models import dateutil
import time
from sleep.models.sleep import Sleep

@view_config(route_name='home', renderer='home.mako')
def home_view(request):
    # are we logged in?
    if request.user:
        # has the user inserted a new sleep record?
        if 'start_date' in request.POST:
            start_date = request.POST.get('start_date')
            
            start_time = request.POST.get('start_time')
            start_ampm = request.POST.get('start_ampm')
            
            end_time = request.POST.get('end_time')
            end_ampm = request.POST.get('end_ampm')

            quality = request.POST.get('quality')
            
            if not start_date or not start_time or not start_ampm \
            or not end_time or not end_ampm or not quality:
                request.session.flash('fill in all the boxes')
            else:
                v = True
                
                # i don't even
                if start_ampm not in ['am', 'pm'] \
                or end_ampm not in ['am','pm']:
                    v = False
                else:
                    st = start_time.split(',')
                    et = end_time.split(',')
                    
                    if not dateutil.valid_time(st) or not dateutil.valid_time(et):
                        v = False
                        request.session.flash('invalid start/end times')
                        
                    # format the users inputted times
                    st = dateutil.format_input_time(st,start_ampm)
                    et = dateutil.format_input_time(et,end_ampm)

                    # how could they even screw this up
                    if quality not in map(str,range(-5,6)):
                        v = False
                        
                    # verify the date
                    if not dateutil.verify_date(start_date):
                        v = False
                        request.session.flash('invalid start date')
                    
                # submit the sleep record
                if v:
                    sleep_record = Sleep(start=','.join(st),
                                         end=','.join(et),
                                         date=start_date,
                                         user_id=request.user.id,
                                         quality=quality,
                                         submitdate=int(time.time()))
                    request.DBSession.add(sleep_record)
                    
        # get this user's sleep records
        output = []
        
        for r in request.user.records:
            output.append({'id' : r.id,
                           'date': dateutil.format_db_date(r.date),
                           'start': dateutil.format_db_time_o(r.start),
                           'end': dateutil.format_db_time_o(r.end),
                           'quality': r.quality,
                           'duration' : '%.2f' % round(r.duration() / float(60*60),2)})
        
        return {'records' : output}
    else:
        return {}