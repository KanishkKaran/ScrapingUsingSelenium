#Open Jupyter Notebook and run following commands:
from selenium import webdriver

#import selenium package with webdriver to run the type of browser you will run to scrape data
from selenium.webdriver.support.ui import Select

#import selenium.webdriver.support.ui is an interface which will help you to find the ui element within the webbrowser.
import pandas as pd
#By now, you'd know importing pandas is required to analyze datasets.

%matplotlib inline
#matplotlib is magic function of Python which will helps in plotting matplot functions. The function matplotlib helps in developing behind-the-scenes setup for IPython to work correctly hand. 
driver = webdriver.Chrome()
#make sure you are using Chrome as your default browser, if not then change your driver to default browser
driver.get('URL')
#asking the variable driver to get the website that you want to scrape.
objects = driver.find_elements_by_class_name('object_name')
#Here we are looking at the type of elements that we want to grab. 
for object in objects:
#For statements, the ususal. If you still don't get it. I'd recommend reading this: http://www.bowdoin.edu/~ltoma/teaching/cs107/fall05/Lectures-Handouts/for.pdf
    print(object.text)
#Just a regular command for printing statements what you've scraped. 
objects2 = driver.find_elements_by_class_name('object_2_name')
#Kind of what we did above
for object2 in objects2:
    print(object2.text)
#steps repeated
data = []
infos = driver.find_elements_by_class_name('object_3_name')
#Looking for another data class. 
for info in infos:
    datapoint = {}
    #Closing datatype in a frame
    datapoint['Object'] = info.find_element_by_class_name('Object_name').text
    #Finding the element in HTML from which we are required to scrape the information 
    datapoint['Object2'] = info.find_element_by_class_name('Object_2_name').text
    #Same as above for different variable
    data.append(datapoint)
pd.DataFrame(data)
#Putting values in frame
df = pd.DataFrame(data)
df.to_csv('hm-sales.csv', index=False)
#Saving data in a csv file
