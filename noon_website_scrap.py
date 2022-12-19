# pip3 install requests
import requests

# // pip3 install beautifulsoup4
from bs4 import BeautifulSoup

# // pip3 install pandas  
import pandas as pd

url = f"https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/"
response = requests.get(url)
response = response.content
soup = BeautifulSoup(response, 'html.parser')

div = soup.find('div', class_='sc-2e5fceb-7 iFjxuh grid')
span = div.find_all('span',class_="sc-5e739f1b-0 gEERDr wrapper productContainer  ")
