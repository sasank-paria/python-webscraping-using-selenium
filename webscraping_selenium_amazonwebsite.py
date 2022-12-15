from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from openpyxl import Workbook

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//input[contains(@id,'search')]").send_keys("samsung phones")
driver.find_element(By.XPATH,"//input[@value='Go']").click()

driver.find_element(By.XPATH, "//span[text()='Samsung']").click()
phonenames=driver.find_elements(By.XPATH,"//span[contains(@class,'a-size-medium a-color-base a-text-normal')]")
price=driver.find_elements(By.XPATH,"//span[contains(@class,'a-price-whole')]")

phonelist=[]
pricelist=[]

for phone in phonenames:
    print(phone.text)
    phonelist.append(phone.text)


for x in price:
    print(x.text)
    pricelist.append(x.text)

finallist=zip(phonelist,pricelist)

# for data in list(finallist):
#     print(data)
#if we iterate the list then further we cant use the finallist in sheet

wb=Workbook()
sheet1=wb.active
sheet1.title="amazonwebscraping"
sheet1.append(["Phone Name","Price"])

for x in list(finallist):
    sheet1.append(x)

wb.save("amazonwebscraping.xlsx")