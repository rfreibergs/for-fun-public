#importi
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from schwifty import IBAN

import random

#parametri
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tortugacasino.com/en")
poga1 = '//*[@id="modal-register-access"]'
poga2 = '//*[@id="stepOneForm"]/div[9]/a'
poga3 = '//*[@id="registerButton"]/span'
poga4 = '//*[@id="logged-close-btn"]'
keksis1 = '//*[@id="registrationTAC"]'
keksis2 = '//*[@id="privacyPolicy"]/label'

acc_count = 200

#datubazes
vards = ["Jānis", "Pēteris", "Juris", "Dainis", "Artūrs"]
uzvards = ["Ozoliņš", "Bērziņš", "Kalniņš", "Krūmiņš", "Ivanovs"]
username = ["killer", "slayer", "hunter", "stalker", "gambler"]
email = ["@gmail.com", "@inbox.lv", "@icloud.com", "@mail.ru", "@yandex.ru"]
adrese = ["Vaļnu", "Skuju", "Rīgas", "Smilšu", "Brīvības"]
pilseta = ["Rīga", "Daugavpils", "Jelgava", "Liepāja", "Ventspils"]

#datumi (vienkarsibas del dobm vienmer ir oktobris)
dobd = random.randint(10, 29)
doby = random.randint(60, 100)

for x in range(acc_count + 1):
    #pirmais solis
    driver.find_element_by_xpath(poga1).click()
    #driver.find_element_by_id("register-username").send_keys(random.choice(username) + str(random.randrange(1000000)) + "___dobromir_got_hacked" + str(x+1))
    driver.find_element_by_id("register-username").send_keys(random.choice(username) + str(random.randrange(1000000)))
    driver.find_element_by_id("register-email").send_keys(str(random.randrange(1000000000000)) + random.choice(email))
    driver.find_element_by_xpath('//*[@id="stepOneForm"]/div[3]/input').send_keys("Parole123")
    driver.find_element_by_xpath('//*[@id="stepOneForm"]/div[4]/input').send_keys("Parole123")
    driver.find_element_by_id("country-dropdown").send_keys("Latvia")
    driver.find_element_by_id("dateOfBirth_day").send_keys(dobd)
    driver.find_element_by_id("dateOfBirth_month").send_keys("October")
    driver.find_element_by_id("dateOfBirth_year").send_keys("19" + str(doby))
    driver.find_element_by_id("currency-dropdown").send_keys("EUR")
    driver.find_element_by_xpath(poga2).click()
    driver.implicitly_wait(1)

    #otrais solis

    driver.find_element_by_xpath('//*[@id="stepTwoForm"]/div[1]/div[1]/input').send_keys(random.choice(vards))
    driver.find_element_by_xpath('//*[@id="lastName"]/input').send_keys(random.choice(uzvards))
    driver.find_element_by_id("phoneCodes-dropdown").send_keys("+371")
    driver.find_element_by_id("regMobilePhoneNumber").send_keys("2" + str(random.randint(1000000, 10000000)))
    driver.find_element_by_xpath('//*[@id="stepTwoForm"]/div[3]/div[1]/input').send_keys(random.choice(pilseta))
    driver.find_element_by_xpath('//*[@id="cityPostalCodeWrapper"]/input').send_keys("LV-" + str(random.randint(1000, 10000)))
    driver.find_element_by_xpath('//*[@id="stepTwoForm"]/div[4]/input').send_keys(random.choice(adrese) + " iela " + str(random.randrange(200)) + ", k-" + str(random.randint(1, 6)) + ", dzīvoklis " + str(random.randrange(100)))
    driver.find_element_by_xpath(keksis1).click()
    driver.find_element_by_xpath(keksis2).click()

    #REGISTRACIJA!!!!!!
    driver.find_element_by_xpath(poga3).click()
    #driver.get("https://tortugacasino.com/en")
