#For SNOW
import time
from splinter.browser import Browser
lst=list()

patch_no=raw_input("enter new patch number(eg:R106):")
DC_num=[12,17]
print 'enter implementation date in yyyy,mm,dd order and enter friday\'s date,script will adjust the date and time by itself'
yr=raw_input('year:')
mnth=raw_input('month:')
dayf=raw_input('day:')
dayt=str(int(dayf)-1)
if int(dayt)<10:
    dayt='0'+str(dayt)
day_splitt=[yr,mnth,dayt]
day_splitf = [yr,mnth,dayf]
datef='-'.join(day_splitf)
datet='-'.join(day_splitt)

    
br = Browser('chrome')
#br.driver.set_window_position(-10000,0)
br.visit('http://xxxxx/login')
br.click_link_by_text("Use external login")
br.fill('sso_selector_id', 'abc@xxx.com')
br.find_by_name('not_important').first.click()
time.sleep(15)
justify='Performing weekly deployment to update Communities to '+patch_no
test_details='QA Team does the testing and deploys on QA test environment. Once it is released and declared as GO from QA/Engineering Team then we deploy on production environments. '
imp='''details'''
plan=''' details'''
val_steps=''' details  '''
def create_ticket(rum,sh,s,e):
    br.find_by_text('Change').first.click()
    br.find_by_id('323bb07bc611227a018aea9eb8f3b35e').first.click()
    with br.get_iframe("gsft_main") as iframe:
        iframe.click_link_by_text('Normal: Changes without predefined plans that require approval and CAB authorization.')
        time.sleep(4)
        num=iframe.find_by_id('sys_readonly.change_request.number')
        lst.append(num.value)
        iframe.fill("sys_display.change_request.u_category","Change > Patch Release")
        iframe.fill("sys_display.change_request.business_service",rum)
        iframe.find_by_id('change_request.u_customer_impact').first.select('no_impact')
        time.sleep(5)
        iframe.fill('sys_display.change_request.assigned_to','xxxxx')
        iframe.find_by_id('change_request.u_ccm_notify').first.select('No')
        iframe.find_by_id('sys_select.change_request.u_data_protection_type').first.select('3133d41bdb943200076670adbf961914')
        iframe.find_by_id('change_request.priority').first.select('3')
        iframe.fill('change_request.short_description',sh)
        iframe.fill('change_request.description',sh)
        iframe.find_by_text('Planning').first.click()
        iframe.fill('change_request.justification',justify)
        iframe.fill('change_request.u_pre_test_details',test_details)
        iframe.fill('change_request.change_plan',imp)
        iframe.find_by_id('change_request.u_maintenance_page').first.select('Not Required')
        iframe.find_by_id('change_request.u_pop_up').first.select('No')
        iframe.fill('change_request.backout_plan',plan)
        iframe.fill('change_request.test_plan',val_steps)
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
        iframe.find_by_id('sysverb_insert').click()
        
for dc in DC_num:
    if dc==12:
        env='ABC'
        start=datef+" 02:00:00"
        end=datef+" 03:00:00"
        short_desc=env+" | Weekly Patch "+patch_no
        create_ticket(env,short_desc,start,end)
    
    elif dc==17:
        env='ABC1'
        start=datet+" 17:00:00"
        end=datet+" 18:00:00"
        short_desc=env+" | Weekly Patch "+patch_no
        create_ticket(env,short_desc,start,end)

    
br.quit()    
print lst
            

