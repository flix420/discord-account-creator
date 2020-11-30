from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import requests
import random
import json
import time
import os
import string
import undetected_chromedriver as uc

months = ['December', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']

selection_month = random.choice(months)
selection_day = random.randint(1,28)

email = input("Your email (for infinite emails going to one email visit https://generator.email/blog/gmail-generator): ")
sleeptime = int(input("Sleep time in seconds (recommended to be set to 5 so captcha doesnt rekt you): "))

try:
    int(sleeptime)
except ValueError:
    print('Not a number...')
    os.system("cls")

r2 = requests.get('http://names.drycodes.com/10')
fem = r2.json()
asef = random.choice(fem)
print(f"Username: {asef}")

r3 = requests.get('https://www.dinopass.com/password/simple')
passwd = r3.text
print(f"Password: {passwd}")


driver = uc.Chrome()
driver.get("https://discord.com/register")
enter_searchbar = driver.find_element_by_name("email")
enter_searchbar.send_keys(email)
time.sleep(sleeptime)
enter_user = driver.find_element_by_name("username")
enter_user.send_keys(asef)
time.sleep(sleeptime)
enter_passwd = driver.find_element_by_name("password")
enter_passwd.send_keys(passwd)
time.sleep(sleeptime)
enter_month = driver.find_element_by_id("react-select-2-input")
enter_month.send_keys(selection_month, Keys.ENTER)
time.sleep(sleeptime)
enter_day = driver.find_element_by_id("react-select-3-input")
enter_day.send_keys(selection_day, Keys.ENTER)
time.sleep(sleeptime)
enter_year = driver.find_element_by_id("react-select-4-input")
enter_year.send_keys(random.randint(1988, 1997), Keys.ENTER)
time.sleep(sleeptime)
driver.find_element_by_xpath("//input[@class='inputDefault-3JxKJ2 input-3ITkQf']").click()
driver.find_element_by_xpath("//button[@type='submit']").click()
print('45 seconds to complete the captcha...')
def gettoken():
    time.sleep(45)
    os.system("cls")

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Host': 'discord.com',
        'Accept': '*/*',
        'Accept-Language': 'en-US',
        'Content-Type': 'application/json',
        'Referer': 'https://discord.com/register',
        'Origin': 'https://discord.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

    json = {
        'email': email,
        'password': passwd,
    }

    esafaf = requests.post('https://discord.com/api/v6/auth/login', headers=headers, json=json)
    rab = esafaf.json()
    print(rab['token'])
    file1 = open("tokens.txt","a+")
    file1.write(f"{rab['token']}\n")
    file1 = open("accs.txt","a+")
    file1.write(f"\n\nUsername: {asef}\nEmail: {email}\nPassword: {passwd}\n\n---")


gettoken()
