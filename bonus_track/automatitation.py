from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# WEB SCRAPING WITH SELENIUM

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.bna.com.ar/Personas")
driver.maximize_window()
time.sleep(5)

quoteDate = driver.find_element_by_class_name("fechaCot").text
print(quoteDate)
print("==============================")
thTableCot = driver.find_elements_by_xpath("//*[@id='billetes']/table/thead/tr")

for th in thTableCot:
    print(th.text)
print("==============================")

trTableCot = driver.find_elements_by_xpath("//*[@id='billetes']/table/tbody/tr")

for tr in trTableCot:
    row = tr.text
    print(row)
print("==============================")

# Saving data to a Dataframe

quoteDataFrame = pd.DataFrame(columns=['Moneda', 'Compra', 'Venta', 'Promedio'],
index=range(4))

quoteDataFrame.iloc[0] = row


print(quoteDataFrame)