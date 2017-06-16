import socket
import difflib
import commands
import sys
lst=list()
flag=0

cron_ser=commands.getoutput('ps -A')

if 'cron' not in cron_ser:
    flag=1

with open('/var/spool/cron/tabs/root', 'r') as cron_entry:
    with open('/var/spool/cron/tabs/root.bak', 'r') as file2:
        diff = difflib.unified_diff(
            cron_entry.readlines(),
            file2.readlines(),
            fromfile='cron_entry',
            tofile='file2',lineterm='',n=0
        )

        for line in diff:
            line=line.rstrip()
            if line.startswith('-'):
                lst.append(line)


if len(lst)==0:
    pass
elif len(lst) or flag==1:
    try:
        n=lst[2:]
        if len(n)>0:
            print socket.gethostname(),"\ndifference\n",n,"\n"
    except:
        pass
