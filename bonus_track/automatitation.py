from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.bna.com.ar/Personas")
driver.maximize_window()
time.sleep(5)

quoteDate = driver.find_element_by_class_name("fechaCot").text

thTableCot = driver.find_elements_by_xpath("//*[@id='billetes']/table/thead/tr")

for th in thTableCot:
    print(th.text)

trTableCot = driver.find_elements_by_xpath("//*[@id='billetes']/table/tbody/tr")

for tr in trTableCot:
    print(tr.text)