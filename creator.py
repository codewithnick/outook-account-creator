global domain
domain="@hotmail.com"
userNamePasswordFile = 'NameList.txt'
createdUserNamePasswordFile = 'createdNames.txt'


from randomUserNames import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from random import randint
import time 
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



def create_account(username, password):
    #set up profile for proxy
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    browser = webdriver.Chrome("chromedriver.exe", options=chrome_options)

    #get reddit account creation page
    browser.get('https://signup.live.com/signup')
    browser.find_element_by_id('MemberName').send_keys(username+domain)
    time.sleep(1)
    browser.find_element_by_id('iSignupAction').click()
    time.sleep(3)
    browser.find_element_by_id('PasswordInput').send_keys(password)
    time.sleep(1)
    browser.find_element_by_id('iSignupAction').click()
    time.sleep(3)
    name=''.join([i for i in username if not i.isdigit()])
    name=name.split("_")
    browser.find_element_by_id('FirstName').send_keys(name[0])
    browser.find_element_by_id('LastName').send_keys(name[1])
    time.sleep(1)
    browser.find_element_by_id('iSignupAction').click()
    time.sleep(3)
    select = Select(browser.find_element_by_id('BirthMonth'))
    # select by visible text
    select.select_by_visible_text('January')
    select = Select(browser.find_element_by_id('BirthDay'))
    # select by visible text
    select.select_by_visible_text('1')
    browser.find_element_by_id('BirthYear').send_keys('2000')
    time.sleep(1)
    browser.find_element_by_id('iSignupAction').click()
    #solve the captcha    
    print("\n\n")
    print("*"*100)
    myinput = input("\n[*] Solve captcha, click signup on browser, then press enter here...\n enter 'r' as input if some problem occurs, to skip this username" + '\n')
    if (myinput == 'r'):
        browser.quit()
        return False
    else:
        browser.quit()
        return True





def main():
    #run account generator for each user in list
    
    creds = [cred.strip() for cred in open(userNamePasswordFile).readlines()]
    global username,password
    for cred in creds:
        username, password = cred.split(':')
        print('[+] creating account for %s with password %s' % (username,password))
        account_created = create_account(username, password)
        #print('[+] restarting tor for a new ip address...')
        #os.system('service tor restart')
        if account_created:
            created = open(createdUserNamePasswordFile, 'a')
            print('[+] writing name:password to created names...')
            username+=domain
            created.write(username + ':' + password + '\n')
            print('[+] saved username password')
            created.close()
        else:
            print('[-] skipping name ')
        print('[+] deleting name:password from original file...')
        lines = [line.strip() for line in open(userNamePasswordFile).readlines()]
        f = open(userNamePasswordFile, 'w')
        for line in lines:
            if (line != cred):
                f.write(line + "\n")
        f.close()
        time.sleep(0.5)
        
    created.close()

    
main()
