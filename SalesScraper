from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
%matplotlib inline
driver = webdriver.Chrome()
#make sure you are using Chrome as your default browser, if not then change your driver to default browser
driver.get('http://www.hm.com/us/products/sale/home')
products = driver.find_elements_by_class_name('product-title')
for product in products:
    print(product.text)
prices = driver.find_elements_by_class_name('product-price')
for price in prices:
    print(price.text)
data = []
infos = driver.find_elements_by_class_name('product-info')
for info in infos:
    datapoint = {}
    datapoint['Products'] = info.find_element_by_class_name('product-title').text
    datapoint['Prices'] = info.find_element_by_class_name('product-price').text
    data.append(datapoint)
pd.DataFrame(data)
df = pd.DataFrame(data)
df.to_csv('hm-sales.csv', index=False)
