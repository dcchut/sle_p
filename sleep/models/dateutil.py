# takes a list as input
def valid_time(t):
    # t doesn't have two components
    if len(t) != 2:
        return False
    
    # need t to only have digits
    if not t[0].isdigit() or not t[1].isdigit():
        return False
    
    # need first component of t to be in 1,...,12
    if int(t[0]) not in range(1,13):
        return False
    
    # need first component of t to be in 0, 10, .., 50
    if int(t[1]) not in range(0,60,10):
        return False
    
    # otherwise we're all good
    return True
    
# takes a valid list as input    
def format_input_time(t, ampm):
    # this should really be true
    assert(valid_time(t))
    
    # we want to replace 12's with 0's 
    if int(t[0]) == 12:
        t[0] = '0'
        
    # add twelve hours if we're in the PM
    if ampm == 'pm':
        t[0] = str(int(t[0])+12)
        
    return t
    
# takes a database time and formats it for output
def format_db_time_o(t):
    t = map(int, t.split(','))
    
    # are we in the PM?
    pm = t[0] >= 12
    
    if t[0] > 12:
        t[0] -= 12
        
    # we now format our output string
    o = str(t[0]).zfill(2) + ':' + str(t[1]).zfill(2) + ' '
    
    if pm:
        o += 'PM'
    else:
        o += 'AM'
    
    return o
    
# format a date nicely
def format_db_date(d):
    d = d.split('/')
    d[1] = d[1].zfill(2)
    return '/'.join(d)
    
# takes a string as input, verifies it as correctly being in dd/mm/yy format
def verify_date(d):
    # we best hope that, after removing all the slashes, everything thats left is a digit
    if not d.replace('/','',).isdigit():
        return False
    
    # split the date up into (hopefully!) 3 components
    d = map(int, d.split('/'))
    
    if len(d) != 3:
        return False
    
    # we do a pretty lazy date check here; 
    # if i were a better programmer I'd look up the manual to figure out how it should be done
    if d[0] not in range(1,32) or d[1] not in range(1,13) or d[2] not in range(2012,2020):
        return False
    
    return True
    
    
    