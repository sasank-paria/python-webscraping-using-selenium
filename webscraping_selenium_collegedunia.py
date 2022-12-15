from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from openpyxl import Workbook
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://collegedunia.com/usa/college/1090-harvard-university-cambridge")
driver.implicitly_wait(10)


driver.find_element(By.XPATH, "//a[text()='Courses & Fees']").click()

#courses
courses = driver.find_elements(By.XPATH,"//h2[contains(@class,'jsx-3847118977 jsx-2133140133')]/a") #this is for anchor tag text 
for x in courses:
    print(x.text)

#fees
fees = driver.find_elements(By.XPATH,"//span[contains(@class,'jsx-3847118977 jsx-2133140133 fees font-weight-bolder')]")
for y in fees:
    print(y.text)

#duration
duration = driver.find_elements(By.XPATH,"//span[contains(@class,'jsx-3847118977 jsx-2133140133 text-capitalize')]")
for z in duration:
    print(z.text)

#scholarship data from table
driver.find_element(By.XPATH, "//a[text()='Scholarship']").click()

row_count = len(driver.find_elements(By.XPATH,"//*[@id='__next']/div[2]/section/div/div[1]/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]/table/tbody/tr"))

col_count = len(driver.find_elements(By.XPATH,"//*[@id='__next']/div[2]/section/div/div[1]/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]/table/tbody/tr[2]/td"))
print(row_count)
print(col_count)

