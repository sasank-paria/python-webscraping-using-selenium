import requests
import requests
import lxml
from bs4 import BeautifulSoup

# url ="https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/"
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
#     "Accept-Language": "en-US,en;q=0.9"
# }

# response = requests.get(url, headers=header)

# soup = BeautifulSoup(response.content, "lxml")

# div = soup.find(class_="sc-2e5fceb-7 iFjxuh grid")

# var1 = "https://www.noon.com"
# #first page products url
# for i in range(0,51):
#  product_url = div.find_all('a')[i].get('href')
#  product_url_og=("".join([var1,product_url]))



#from second page onwards
for i in range(2,67):
    url2 = f"https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?limit=50&page={i}&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc"
    header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.get(url2, headers=header)

    soup = BeautifulSoup(response.content, "lxml")

    div = soup.find('div',class_="sc-2e5fceb-7 iFjxuh grid")
    
    var1 = "https://www.noon.com"
    #first page products url
    
    for i in range(0,51):
        try:
            product_url = div.find_all('a')[i].get('href')
            product_url_og=("".join([var1,product_url]))
            
            response3 = requests.get(product_url_og , headers = header)
            soup3 = BeautifulSoup(response3.content, "lxml")
            
            product_name = soup3.find('h1',class_="sc-7a158dd5-14 hNzvXk").get_text()
            print(product_name)
            
            model_no = soup3.find('div',class_="modelNumber").text
            print(model_no)

            price = soup3.find('div',class_="priceNow").text
            res = ''.join(filter(lambda i: i.isdigit(), price))
            print(float(res))

            saving = soup3.find('div',class_="priceSaving")
            discount = saving.find('span',class_="profit").text
            res = ''.join(filter(lambda i: i.isdigit(), discount))
            print(res)

            soldby=soup3.find('div',class_="sc-95752873-0 VQRHP").text
            print(soldby)

            seller_rating = soup3.find('')


        except:
            print("error occured")




 
    
       