import datetime 
import datetime
import pytz
from datetime import datetime



def Duration(s,e):
    IST = pytz.timezone('Asia/Kolkata')
    get_date = s.split()
    year = get_date[0].split('-')
    hourly_time = get_date[1].split(':')
    y,mo,d= int(year[0]),int(year[1]),int(year[2])
    h,mi,se = int(hourly_time[0]),int(hourly_time[1]),int(hourly_time[2])
    start = datetime(y, mo, d, h, mi, se)        
    now  = datetime.now(IST).replace(tzinfo=None)                         
    dif_start =  str(now - start)
    get_margin = e.split()#submission time
    year = get_margin[0].split('-')
    hourly_time = get_margin[1].split(':')
    y,mo,d = int(year[0]),int(year[1]),int(year[2])
    h,mi,se = int(hourly_time[0]),int(hourly_time[1]),int(hourly_time[2])
    end = datetime(y, mo, d, h, mi, se)        
    now  = datetime.now(IST).replace(tzinfo=None)                         
    dif_end =  str(end - now)
    if dif_start[0] != '-' and dif_end[0] != '-':
        return 1
    if dif_start[0] == '-' and dif_end[0] != '-':
        return 2
    if dif_start[0] != '-' and dif_end[0] == '-':
        return 3
    else:
        return 4

