from jira import JIRA
options={
        'server':'https://jira.successfactors.com/',
        }
while True:
        try:
                usrname=raw_input("enter ur username:")
                passwd=raw_input("enter ur password:")
                jira=JIRA(options,basic_auth=(usrname,passwd),validate=True)
                break
        except Exception:
                print 'wrong username or password.Please try again'
                continue

lists=[]
patch_no=raw_input("enter new patch number(eg:1701):")
DC_num=[2,4,8,10,12,15,17,18,19]
print 'enter implementation date in yyyy,mm,dd order and enter friday\'s date,script will adjust the date and time by itself'
yr=raw_input('year:')
mnth=raw_input('month:')
dayf=raw_input('day:')
dayt=str(int(dayf)-1)
day_splitt=[yr,mnth,dayt]
day_splitf = [yr,mnth,dayf]
datef='-'.join(day_splitf)
datet='-'.join(day_splitt)


def send_mail(recipient, subject, message): 

        import smtplib
        from email.MIMEMultipart import MIMEMultipart
        from email.MIMEText import MIMEText

        username = "XXX@gmail.com"
        password = "XXXX"
        print 'preparing for mailing all the CMSDs created'
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = ",".join(recipient)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        try:
                print 'sending mail to ' + ",".join(recipient) + ' on ' + subject

                mailServer = smtplib.SMTP('smtp.gmail.com', 587)
                mailServer.ehlo()
                mailServer.starttls()
                mailServer.ehlo()
                mailServer.login(username, password)
                mailServer.sendmail(username, recipient, msg.as_string())
                mailServer.close()

        except Exception:
                print 'error! mail not set'
                
def assign_values(a,b,c,d,data_protection,start,end):
        smry="Mobile | MobTrain-"+str(patch_no)+" Monthly Release | " + a+" "+d
        descript="""details """
        test_details="Successful deployment to release version "+str(patch_no)
        justification="This ticket is for monthly patch deployment"
        imp_steps="details"
        back_steps="""details"""
        validate="""details """

        values = {
                'project' : 'CMSD',
                'issuetype' : 'Change Request',
                'customfield_16584' : { 'value' : 'Low' },
                'summary' : smry,
                'customfield_17680' : { 'value' : 'Low' },
                'customfield_17681' : { 'value' : 'Low' },
                'customfield_17682' : { 'value' : 'Low' },
                'customfield_17683' : { 'value' : 'Low' },
                'customfield_17684' : { 'value' : 'Low' },
                'customfield_16583' : {'value':'App', 'child': {'value':'Update/Upgrade'}},
                'components' : [{'name': 'Mobile'}],
                'customfield_15282' : {'value':data_protection},
                'customfield_10802' : { 'value' : a },
                'customfield_16590' : { 'id' : Ztime },
                'customfield_10842' : { 'id' : c },
                'customfield_16794' : {'value':'None'},
                'customfield_17055' : {'value':'No'},
                'customfield_17056' : { 'value' : 'Not Required' },
                'customfield_17057' : { 'value' : 'No' },
                'customfield_16814' : start,
                'customfield_16815' : end,
                'description' : descript,
                'customfield_17426' : test_details,
                'customfield_17427' : justification,
                'customfield_17058' : imp_steps,
                'customfield_16800' : back_steps,
                'customfield_16801' : validate,
                'customfield_16802' : { 'name' : 'skumari' },
                'customfield_17059' : [{ 'value' : 'TechOwn - Mobile' }],
                'customfield_17060' : [{ 'value' : 'BusOwn - Mobile' }],
                                        }
        new_issue = jira.create_issue(fields=values)
        jira.assign_issue(new_issue, 'jira name')
        #print new_issue.key
        key=a+" "+j+":"+str(new_issue.key)
        #print key
        lists.append(key)

for i in range(9):
        DC=DC_num[i]
        if DC==2:
                actual_DC="DC"+str(DC)+' - '+"Amsterdam2"
                Ztime="21745"
                data='European Union Data Protection'
                env=['Prod','Sales','Preview']
                for j in env:
                        if j=='Prod':
                                actual_env='11668'
                                start=datet+'T16:30:00.000-0700'
                                end=datet+'T22:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Sales':
                                actual_env='11930'
                                start=datet+'T16:30:00.000-0700'
                                end=datet+'T22:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Preview':
                                actual_env='17660'
                                start=datet+'T16:30:00.000-0700'
                                end=datet+'T22:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
        elif DC==4:
                actual_DC="DC"+str(DC)+' - '+"Chandler1"
                Ztime="21744"
                data='No Data Protection Regulation'
                env=['Prod','Sales','Preview']
                for j in env:
                        if j=='Prod':
                                actual_env='11668'
                                start=datet+'T12:30:00.000-0700'
                                end=datet+'T18:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Sales':
                                actual_env='11930'
                                start=datet+'T12:30:00.000-0700'
                                end=datet+'T18:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Preview':
                                actual_env='17660'
                                start=datet+'T12:30:00.000-0700'
                                end=datet+'T18:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
        elif DC==8:
                actual_DC="DC"+str(DC)+' - '+"Ashburn1"
                Ztime="21744"
                data='No Data Protection Regulation'
                env=['Prod','Sales','Preview']
                for j in env:
                        if j=='Prod':
                                actual_env='11668'
                                start=datet+'T12:30:00.000-0700'
                                end=datet+'T18:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Sales':
                                actual_env='11930'
                                start=datet+'T12:30:00.000-0700'
                                end=datet+'T18:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Preview':
                                actual_env='17660'
                                start=datet+'T12:30:00.000-0700'
                                end=datet+'T18:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
        elif DC==10:
                actual_DC="DC"+str(DC)+' - '+"Sydney1"
                Ztime="21746"
                data='No Data Protection Regulation'
                env=['Prod','Preview']
                for j in env:
                        if j=='Prod':
                                actual_env='11668'
                                start=datef+'T02:30:00.000-0700'
                                end=datef+'T08:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Sales':
                                actual_env='11930'
                                start=datef+'T02:30:00.000-0700'
                                end=datef+'T08:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Preview':
                                actual_env='17660'
                                start=datef+'T02:30:00.000-0700'
                                end=datef+'T08:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
        elif DC==12:
                actual_DC="DC"+str(DC)+' - '+"Rot1"
                Ztime="21745"
                data='European Union Data Protection'
                env=['Prod','Preview','Bosch']
                for j in env:
                        if j=='Prod':
                                actual_DC="DC"+str(DC)+' - '+'Rot1(Monsoon)'
                                actual_env='11668'
                                start=datet+'T16:30:00.000-0700'
                                end=datet+'T22:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Preview':
                                actual_DC="DC"+str(DC)+' - '+'Rot1(Monsoon)'
                                actual_env='17660'
                                start=datet+'T16:30:00.000-0700'
                                end=datet+'T22:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Bosch':
                                actual_env='11668'
                                start=datet+'T16:30:00.000-0700'
                                end=datet+'T22:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
        elif DC==15:
                actual_DC="DC"+str(DC)+' - '+"Shanghai1"
                Ztime="21747"
                data='No Data Protection Regulation'
                env=['Prod']
                for j in env:
                        if j=='Prod':
                                actual_env='11668'
                                start=datef+'T00:30:00.000-0700'
                                end=datef+'T06:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
        elif DC==17:
                actual_DC="DC"+str(DC)+' - '+"Toronto1"
                Ztime="21744"
                data='No Data Protection Regulation'
                env=['Prod','Preview']
                for j in env:
                        if j=='Prod':
                                actual_env='11668'
                                start=datet+'T12:30:00.000-0700'
                                end=datet+'T18:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Sales':
                                actual_env='11930'
                                start=datet+'T12:30:00.000-0700'
                                end=datet+'T18:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Preview':
                                actual_env='17660'
                                start=datet+'T12:30:00.000-0700'
                                end=datet+'T18:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
        elif DC==18:
                actual_DC="DC"+str(DC)+' - '+"Moscow1"
                Ztime="21748"
                data='No Data Protection Regulation'
                env=['Prod','Preview']
                for j in env:
                        if j=='Prod':
                                actual_env='11668'
                                start=datet+'T19:30:00.000-0700'
                                end=datef+'T01:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Sales':
                                actual_env='11930'
                                start=datet+'T19:30:00.000-0700'
                                end=datef+'T01:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Preview':
                                actual_env='17660'
                                start=datet+'T19:30:00.000-0700'
                                end=datef+'T01:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)

        elif DC==19:
                actual_DC="DC"+str(DC)+' - '+"Sao Paulo1"
                Ztime="21749"
                data='No Data Protection Regulation'
                env=['Prod','Preview']
                for j in env:
                        if j=='Prod':
                                actual_env='11668'
                                start=datet+'T18:00:00.000-0700'
                                end=datet+'T20:00:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Sales':
                                actual_env='11930'
                                start=datet+'T18:30:00.000-0700'
                                end=datet+'T20:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
                        elif j=='Preview':
                                actual_env='17660'
                                start=datet+'T18:30:00.000-0700'
                                end=datet+'T20:30:00.000-0700'
                                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)

print lists
print 'converting lists of CMSDs into string'
string=','.join(lists)
send_mail(['werh@asd.com','xyz@abc.com'], 'CMSD tickets for next Mobile release', string)
