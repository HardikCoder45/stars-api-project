from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

# NASA Exoplanet URL
START_URL = "hhttps://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("C:/Users/inno/Desktop/hardik coder all files/PRO-C127-Student-Boilerplate-Code-main/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scarped_data = []

# Define Exoplanet Data Scrapping Method
def scrape():
    page = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs")
    soup =  BeautifulSoup(page.content,"html.parser")
    table = soup.find_all("table",attrs={"class","wikitable"})
    table_body = table[2].find("tbody")
    table_row = table_body.find_all("tr")
    for row in table_row:
        table_col = row.find_all("td")
        temp_list =[]
        for col_data in table_col:
         
         data = col_data.text.strip()
            
         temp_list.append(data)
      
         scarped_data.append(temp_list)
       
         

        ## ADD CODE HERE ##
     
        



# Calling Method    
scrape()
print(scarped_data)


 
# Define Header
headers = [
"Brown dwarf",	"Constellation",	"Right ascension","Declination",	"App.mag.",	"Distance" , 	"Spectraltype"	,"Mass", "Radius" ,"Discovery year"]

# Define pandas DataFrame   
planet_df_1 = pd.DataFrame(scarped_data, columns=headers)

# Convert to CSV
planet_df_1.to_csv('new_scraped_data.csv',index=True, index_label="id")
    



    
     
    
   
 