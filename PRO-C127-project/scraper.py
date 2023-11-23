from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("C:/Users/inno/Desktop/hardik coder all files/PRO-C127-Student-Boilerplate-Code-main/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scarped_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

 

     

    soup =  BeautifulSoup(browser.page_source,"html.parser")

    table = soup.find("table",attrs={"class","wikitable"})
    table_body = table.find("tbody")
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


star_data = []
print(len(scarped_data))
for i in range(0,len(scarped_data)): 
    star_names = scarped_data[i][1]
    distance = scarped_data[i][3]
    mass = scarped_data[i][5]
    radius = scarped_data[i][6]
    lum = scarped_data[i][7]
        
    required_data = [star_names,distance,mass,radius,lum]
    star_data.append(required_data)
# Define Header
headers = ["star_names","distance","mass","radius","luminosity"]

# Define pandas DataFrame   
planet_df_1 = pd.DataFrame(star_data, columns=headers)

# Convert to CSV
planet_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
    


