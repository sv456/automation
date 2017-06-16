from __future__ import division
import pingdomlib
import datetime
import time
import json
import sys
import xlsxwriter
from collections import OrderedDict
dl=OrderedDict()
dct=OrderedDict()
flag=True
s=''

url=pingdomlib.Pingdom('username','password','secret key')

choice=sys.argv[1]
start_d=sys.argv[2]
end_d=sys.argv[3]
DC=sys.argv[4]
ENV=sys.argv[5]


if choice==0 or DC=='NO':
    print 'Please '
    sys.exit(0)


def xcel_fun(dct):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    global s
    s='data'+timestr+'.xlsx'
    workbook = xlsxwriter.Workbook(s)
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0
    worksheet.write(row, col, "Check Name")
    worksheet.write(row, col + 1, "Uptime")
    row = 0
    col = 0
    for key,val in dct.items():
        row += 1
        worksheet.write(row, col, key)
        worksheet.write(row, col + 1, val)
    workbook.close()

s_date=start_d.split("-")
e_date=end_d.split("-")
yr_s=int(s_date[0])
mth_s=int(s_date[1])
day_s=int(s_date[2])
yr_e=int(e_date[0])
mth_e=int(e_date[1])
day_e=int(e_date[2])

check=url.getChecks()

if DC == 'ALL':
    if choice == 'abc' or choice == 'xyz' or choice == 'pqr':
        D=['DC02','DC04','DC08','DC10','DC12','DC17','DC18','DC19']
    elif choice == 'lmn':
        D=['DC12','DC17']
    elif choice=='qwe':
        D=['DC12','RackSpace','DC17','DC19']
    elif choice=='uio':
        D=['DC02','DC04','DC08','DC10','DC12','DC16','DC17','DC18','DC19']
    elif choice=='tre':
        D=["DC02","DC04","DC08","DC10","DC12","DC12B","DC171","DC17","DC18","DC19"]
           
for i in check:
    l=i.name
    if DC == 'ALL':
        for dc in D:
            if choice in l and dc in l and ENV in l:
                dl[l]=i.id
    else:
        if choice in l and DC in l and ENV in l:
            if DC=='DC17':
                if 'DC171' in l:
                    pass
                else:
                    dl[l]=i.id
            else:
                dl[l]=i.id
        
if flag is False:
    print 'Please '
    sys.exit(0)

for k,v in dl.items():
    check=url.getCheck(v) 
    d = datetime.datetime(yr_s,mth_s,day_s,0,0)
    unixtime_s = int(time.mktime(d.timetuple()))
    if datetime.datetime(yr_e,mth_e,day_e,23,59,59) > datetime.datetime.now():
        l= datetime.datetime.now()
    else:
        l=datetime.datetime(yr_e,mth_e,day_e,23,59,59)
    unixtime_e = int(time.mktime(l.timetuple())) 
    up=0;down=0
    out=check.outages(time_from=unixtime_s,time_to=unixtime_e)
    for j in out:
        time_s=j['timefrom']
        time_e=j['timeto']
        time_start = datetime.datetime.fromtimestamp(time_s)
        timestamp_start = time_start.strftime('%Y-%m-%d %H:%M:%S')
        time_end = datetime.datetime.fromtimestamp(time_e)
        timestamp_end = time_end.strftime('%Y-%m-%d %H:%M:%S')
        if j['status'] == 'up':
                up+=(time_e-time_s)
        elif j['status'] == 'down':
                down+=(time_e-time_s)

    try:
        avg=(float(up)/(up+down))*100
        dct[k]="%0.2f"%avg
    except Exception:
        pass

avg=0
for n in dct.values():
    avg+=float(n)
avg/=len(dct)
dct['AVERAGE AVAILABILITY']="%.3f"%avg

xcel_fun(dct)
s_name=OrderedDict()
s_name['data']=dct
s_name['xl_name']=s
print json.dumps(s_name)
	


    





    
    





