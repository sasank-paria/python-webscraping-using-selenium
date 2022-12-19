import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://stackoverflow.com/questions/51154114/python-request-get-fails-to-get-an-answer-for-a-url-i-can-open-on-my-browser"
response = requests.get(url)
response = response.content
soup = BeautifulSoup(response, 'html.parser')

print(response)
