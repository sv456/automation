
import time
from selenium import webdriver
from splinter.browser import Browser
lst=list()

patch_no_p=raw_input("enter new patch number with R for prod and developer(eg:R426):")
patch_no_s=raw_input("enter new patch number with R for sales(eg:R426):")
DC_num=[2,4,8,10,12,15,17,18,19]
print 'enter implementation date in yyyy,mm,dd order and enter friday\'s date,script will adjust the date and time by itself'
yr=raw_input('year:')
mnth=raw_input('month:')
dayf=raw_input('day:')
days=str(int(dayf)+1)
dayt=str(int(dayf)-1)
if int(dayt)<10:
    dayt='0'+str(dayt)
if int(days)<10:
    days='0'+str(days)
day_splitt=[yr,mnth,dayt]
day_splitf = [yr,mnth,dayf]
day_splits=[yr,mnth,days]
datef='-'.join(day_splitf)
datet='-'.join(day_splitt)
dates='-'.join(day_splits)
    
br = Browser('chrome')
#br.driver.set_window_position(-10000,0)
br.visit('http://sfsf.service-now.com/login')
br.click_link_by_text("Use external login")
br.fill('sso_selector_id', 'sandesh.vishwanath@sap.com')
br.find_by_name('not_important').first.click()
time.sleep(15)

def create_ticket(rum,s,e,patch_no):
    justify='Update JAM to ' + patch_no
    br.find_by_text('Change').first.click()
    br.find_by_id('323bb07bc611227a018aea9eb8f3b35e').first.click()
    with br.get_iframe("gsft_main") as iframe:
        iframe.click_link_by_text('Standard: Select from available pre-approved change templates. These changes require Technical approval. ')
        iframe.click_link_by_text('Standard Application Changes')
        iframe.find_by_id('item_link_7fce939edbd7fe004418f5461d96192f').click()
        time.sleep(4)
        num=iframe.find_by_id('sys_readonly.change_request.number')
        lst.append(num.value)
        iframe.fill("sys_display.change_request.u_category","Change > Patch Release")
        iframe.fill("sys_display.change_request.business_service",rum)
        iframe.find_by_id('change_request.u_customer_impact').first.select('no_impact')
        time.sleep(5)
        iframe.fill('sys_display.change_request.assigned_to','Saneeth Pushpaja Raghavan')
        iframe.find_by_id('sys_select.change_request.u_data_protection_type').first.select('3133d41bdb943200076670adbf961914')
        iframe.find_by_id('change_request.priority').first.select('3')
        iframe.find_by_text('Planning').first.click()
        iframe.fill('change_request.justification',justify)
        iframe.fill('sys_display.change_request.u_validator','Sureshkumar Appuswaami')
        iframe.find_by_text('Schedule').first.click()
        iframe.fill('change_request.u_requested_by_date_data_center_time',s)
        iframe.fill('change_request.u_requested_by_end_data_center_time',e)
        iframe.find_by_css('span.tab_caption_text')[5].click()
        iframe.find_by_id('change_request.u_complexity_of_change').first.select('1')
        iframe.find_by_id('change_request.u_pre_testing').select('2')
        iframe.find_by_id('change_request.u_rollback_plan_difficulty').first.select('3')
        iframe.find_by_id('change_request.u_level_of_impact').first.select('1')
        iframe.find_by_id('change_request.u_scope_of_validation').first.select('2')
        time.sleep(3)
        #iframe.find_by_id('sysverb_insert').click()
        
for dc in DC_num:
    if dc==2:
        env=['JAM DC2','JAM DC2 DEV','JAM DC2 SD']
        for j in env:
            if j=='JAM DC2':
                p=patch_no_p
                start=datet+" 21:00:00"
                end=datet+" 22:00:00"
            elif j=='JAM DC2 DEV':
                p=patch_no_p
                start=datef+" 23:00:00"
                end=dates+" 00:00:00"
            else:
                p=patch_no_s
                start=datef+" 18:00:00"
                end=datef+" 19:00:00"
            short_desc=j+" | "+"Weekly Patch | Update JAM to "+p
            create_ticket(j,start,end,p)
    elif dc==4:
        env=['JAM DC4','JAM DC4 SD']
        for j in env:
            if j=='JAM DC4':
                p=patch_no_p
                start=datef+" 00:00:00"
                end=datef+" 01:00:00"
            else:
                p=patch_no_s
                start=datef+" 20:00:00"
                end=datef+" 21:00:00"
            short_desc=j+" | "+"Weekly Patch | Update JAM to "+p
            create_ticket(j,start,end,p)
    elif dc==8:
        env=['JAM DC8','JAM DC8 SD']
        for j in env:
            if j=='JAM DC8':
                p=patch_no_p
                start=datef+" 00:00:00"
                end=datef+" 01:00:00"
            else:
                p=patch_no_s
                start=datef+" 20:00:00"
                end=datef+" 21:00:00"
            short_desc=j+" | "+"Weekly Patch | Update JAM to "+p
            create_ticket(j,start,end,p)
    elif dc==10:
        env=['JAM DC10']
        start=dates+" 04:00:00"
        end=dates+" 05:00:00"
        for j in env:
            p=patch_no_p
            short_desc=j+" | "+"Weekly Patch | Update JAM to "+p
            create_ticket(j,start,end,p)
    elif dc==12:
        env=['JAM DC12 Monsoon']
        start=datet+" 21:00:00"
        end=datet+" 22:00:00"
        for j in env:
            p=patch_no_p
            short_desc=j+" | "+"Weekly Patch | Update JAM to "+p
            create_ticket(j,start,end,p)
    elif dc==15:
        env=['JAM DC15']
        start=dates+" 01:00:00"
        end=dates+" 02:00:00"
        for j in env:
            p=patch_no_p
            short_desc=j+" | "+"Weekly Patch | Update JAM to "+p
            create_ticket(j,start,end,p)
    elif dc==17:
        env=['JAM DC17']
        p=patch_no_p
        start=datef+" 00:00:00"
        end=datef+" 01:00:00"
        for j in env:
            short_desc=j+" | "+"Weekly Patch | Update JAM to "+p
            create_ticket(j,start,end,p)
    elif dc==18:
        env=['JAM DC18']
        p=patch_no_p
        start=datef+" 00:00:00"
        end=datef+" 01:00:00"
        for j in env:
            short_desc=j+" | "+"Weekly Patch | Update JAM to "+p
            create_ticket(j,start,end,p)
    elif dc==19:
        env=['JAM DC19']
        p=patch_no_p
        start=datef+" 01:00:00"
        end=datef+" 03:00:00"
        for j in env:
            short_desc=j+" | "+"Weekly Patch | Update JAM to "+p
            create_ticket(j,start,end,p)


br.quit()
print lst
            

    
