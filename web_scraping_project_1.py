# -*- coding: utf-8 -*-
"""web scraping project 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XJUYN-uSc59F41TwDhFg8xMG_8U5uHfe
"""

#Web scrapping project

#install beautiful
!pip install beautifulsoup4

# importing libraries
from bs4 import BeautifulSoup
import requests

# Assign your link to a variable
link = 'https://en.wikipedia.org/wiki/List_of_African_countries_by_area'

# use request to get the raw HTML content from the website
HTML_script = requests.get(link)

HTML_script

# We now extract the text from the HTML_script
text_script = HTML_script.text

text_script

# Where 'html.parser' is a processing tool
useful_text = BeautifulSoup(text_script, "html.parser") 
#We can now print the useful_text using prettify module.
print(useful_text.prettify())

print(useful_text.title.text)

print(useful_text.p.text)

#table = useful_text.find('table', {'class': "wikitable sortable"})

#find where table is located in text_script (HTML_script.text)
table = useful_text.find('table')
table.prettify()

#find all the table rows using find_all
table_rows = table.find_all('tr')

countries = [row.find('a').text for row in table_rows[1:]]
print(countries)

Area = [row.find_all('td')[2].text.strip() for row in table_rows[1:]]
    
print(Area)

Rank = [row.find_all('td')[0].text.strip() for row in table_rows[1:]]
    
print(Rank)

#converting info into dataframe
import pandas as pd
df = pd.DataFrame()
df['Rank'] = Rank
df['Country'] = countries
df['Area'] = Area

df.head()

# use lambda function to split the area column into area(km2) and area(sq mi)
area_func = lambda x:x.split(' ')[0]
df['Area (km2)'] = df['Area'].apply(area_func)

area_func = lambda x:x.split(' ')[-1]
df['Area (sq mi)'] = df['Area'].apply(area_func)

#drop the initial Area column to avoid redundancy of variables
df = df.drop('Area', axis = 1)

#load the first 10 data in the dataframe
df.head(10)