import time

import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



questionTxt = sys.argv[1]

with open(questionTxt, 'r', encoding='utf-8') as file:
    question = file.read()

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")

chrome_service = Service(executable_path='/usr/bin/chromedriver')

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://duckduckgo.com/?q=DuckDuckGo+AI+Chat&ia=chat&duckai=1")



btnConnect = driver.find_element(By.CSS_SELECTOR, ".kaxgJ3vkiSFrBaRFcglY")
btnConnect.click()

actions = ActionChains(driver)

actions.send_keys(Keys.TAB)
time.sleep(0.2)
actions.send_keys(Keys.TAB)
time.sleep(0.2)
actions.send_keys(Keys.TAB)
time.sleep(0.2)
actions.send_keys(Keys.TAB)

actions.perform()

time.sleep(0.2)

actions.send_keys(Keys.ENTER).perform()

time.sleep(1)

inputDuck = driver.find_element(By.CSS_SELECTOR, ".JRDRiEf5NPKWK43sArdC")
inputDuck.send_keys(question, Keys.ENTER)

time.sleep(7)

div_element = driver.find_element(By.CSS_SELECTOR, ".VrBPSncUavA1d7C9kAc5")

text = div_element.text

with open('reponse.txt', 'w', encoding='utf-8') as fichier:
    fichier.write(text)