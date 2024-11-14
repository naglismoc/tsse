''' BŪTINA
pip install undetected-chromedriver
pip install setuptools
'''

import time
from selenium.webdriver.common.by import By
from selenium import webdriver

''' alternatyva:
kai kurie puslapiai mato, kad naudojamas seleniumas ir nuo jo saugosi, tad galime naudoti kitą driverį.
import undetected_chromedriver as uc # importas
# driver = uc.Chrome(use_subprocess=True, suppress_welcome=True) Ędriver objekto sukūrimas
minusas - mėto neaiškius erorus konsolėje
'''
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://skelbiu.lt")
btn  = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
btn.click()

driver.find_element(By.ID, 'searchKeyword').send_keys("raktai")
driver.find_element(By.ID, 'searchButton').click()
tekstas =  driver.find_element(By.XPATH,'//*[@id="body-container"]/div[2]/div[1]/ul/li/span')
print(f'rasta {tekstas.text} skelbimų.')

time.sleep(1) #palaukimas fiksuotą laiką sekundėmis


# driver.quit() #baigiame darbą
