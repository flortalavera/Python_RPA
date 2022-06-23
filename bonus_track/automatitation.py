from selenium import webdriver
from sqlalchemy import column
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# WEB SCRAPING WITH SELENIUM

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.bna.com.ar/Personas")
driver.maximize_window()
time.sleep(5)

# headboards
thDate = driver.find_element_by_class_name("fechaCot").text
thBuy = driver.find_element_by_xpath("//*[@id='billetes']/table/thead/tr/th[2]").text
thSale = driver.find_element_by_xpath("//*[@id='billetes']/table/thead/tr/th[3]").text

# Types curency
tdDolar = driver.find_element_by_xpath("//*[@id='billetes']/table/tbody/tr[1]/td[1]").text
tdEuro = driver.find_element_by_xpath("//*[@id='billetes']/table/tbody/tr[2]/td[1]").text
tdReal = driver.find_element_by_xpath("//*[@id='billetes']/table/tbody/tr[3]/td[1]").text

# Values of buy
tdDolarBuy = driver.find_element_by_xpath("//*[@id='billetes']/table/tbody/tr[1]/td[2]").text
tdEuroBuy = driver.find_element_by_xpath("//*[@id='billetes']/table/tbody/tr[2]/td[2]").text
tdRealBuy = driver.find_element_by_xpath("//*[@id='billetes']/table/tbody/tr[3]/td[2]").text

# Values of sale
tdDolarSale = driver.find_element_by_xpath("//*[@id='billetes']/table/tbody/tr[1]/td[3]").text
tdEuroSale = driver.find_element_by_xpath("//*[@id='billetes']/table/tbody/tr[2]/td[3]").text
tdRealSale = driver.find_element_by_xpath("//*[@id='billetes']/table/tbody/tr[3]/td[3]").text


print("==============================")

# Saving data to a Dataframe

quoteDataFrame = pd.DataFrame({
    'Moneda': [tdDolar, tdEuro, tdReal],
    thBuy: [tdDolarBuy, tdEuroBuy, tdRealBuy],
    thSale: [tdDolarSale, tdEuroSale, tdRealSale],
}, index=range(3))


quoteDataFrame.to_csv("quoteDataFrame.csv", index=False)