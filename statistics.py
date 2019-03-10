from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from plyer import notification
import time

#chrome_params
chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 3)
driver.get("https://ops.klondaika.lv/")

#user_params
login ="LOGINS"
parole = "PAROLE"
timeout = 2
lastreg = [0]
lastpay = [0]
iteracija = 0
kill = ""

#login
driver.find_element_by_xpath('/html/body/ui-view/div/div[2]/div/form/div/div[2]/input').send_keys(login)
driver.find_element_by_xpath('/html/body/ui-view/div/div[2]/div/form/div/div[3]/input').send_keys(parole)
driver.find_element_by_xpath('/html/body/ui-view/div/div[2]/div/form/div/div[5]/button').click()
confirm = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[1]/div/div/div/div/div/div[1]/ul[1]/li[1]/a")))

def lookup():
    driver.get('https://ops.klondaika.lv/admin/#/customers#4')
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="customers"]/tbody/tr[1]/td[2]')))
    lastreg.insert(0, int(driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr[1]/td[2]').text))

    driver.get('https://ops.klondaika.lv/admin/#/payments#4')
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="payments"]/tbody/tr[1]/td[2]')))
    lastpay.insert(0, int(driver.find_element_by_xpath('//*[@id="payments"]/tbody/tr[1]/td[2]').text))

while kill:
    lookup()
    if iteracija is 0:
        messageprint='Pedeja registracija: ' + str(lastreg[0]) + '\nPedejais maksajums: ' + str(lastpay[0])
        titleprint='Statistika'
    else:
        messageprint='Jaunas registracijas: ' + str(lastreg[0] - lastreg[1]) + '\nJauni maksajumi: ' + str(lastpay[0] - lastpay [1])
        titleprint='Pedejo ' + str(timeout) + ' minusu statistika'
    notification.notify(
        message=messageprint,
        title=titleprint,
        app_name='Dench',
        app_icon="dench.ico",
        timeout=5,
        toast=True
        )
    iteracija = iteracija + 1

    time.sleep(60*timeout)
