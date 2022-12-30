from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
service = Service('C:\Development\chromedriver.exe')
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(url='https://personal-python-web.onrender.com/')

XPath_element = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/h1')
print(XPath_element.text)

driver.quit()