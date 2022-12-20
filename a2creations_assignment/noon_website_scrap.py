import requests
import pandas as pd
import lxml
from bs4 import BeautifulSoup
import datetime

data = []
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

            #product url
            product_url = div.find_all('a')[i].get('href')
            product_url_og=("".join([var1,product_url]))
            
            response3 = requests.get(product_url_og , headers = header)
            soup3 = BeautifulSoup(response3.content, "lxml")
            
            #product name
            product_name = soup3.find('h1',class_="sc-7a158dd5-14 hNzvXk").get_text()
            #print(product_name)
            
            #model no
            model_no = soup3.find('div',class_="modelNumber").text
           # print(model_no)
            
            #product price
            price = soup3.find('div',class_="priceNow").text
           # product_price = ''.join(filter(lambda i: i.isdigit(), price))
           # print("price:",price[4:10])
            
            #discount
            saving = soup3.find('div',class_="priceSaving")
            discount = saving.find('span',class_="profit").text
            discount_perc = ''.join(filter(lambda i: i.isdigit(), discount))
           # print(discount_perc)
            
            #seller name
            soldby=soup3.find('div',class_="sc-95752873-0 VQRHP").text
           # print(soldby)
            
            #seller rating
            seller_rating = soup3.find('div',class_="sc-7161241a-3 bSmJAt")
            rating=seller_rating.find('span',class_="sc-e568c3b8-1 bFgxSY").text
           # print(rating)

            #product rating
            p_rating=soup3.find('span',class_="sc-e568c3b8-1 bFgxSY").text
           # print("product rating " , p_rating)

            #currency
            currency = soup3.find('div',class_="priceNow").text
          #  print(currency[0:3])

            #position
            position = soup3.find('div',class_="sc-54ed93c4-2 elMEYP").text
          #  print("position : ",position)

            #brand
            brand = soup3.find('div',class_="sc-7a158dd5-13 kqGPPJ").text
          #  print("brand : ",brand)

            #market
            market = soup3.find('div',class_="sc-b823bcb8-0 jYIGEK")
            market_place = market.find('img').attrs['alt']
           # print("market : ",market_place)

           # stocks left
            # try:
            #     stocks = soup3.find('div',class_="sc-7705b45-0 eDpeUK").text
            #     stocks_left = ''.join(filter(lambda i: i.isdigit(), stocks_left))
            #   #  print("stocks left : ",stocks_left)
            # except:
            #     print("no data available")
            #     ct = datetime.datetime.now()
            #     data.append([ct,product_url_og,product_name,model_no,price[4:10],discount_perc,soldby,rating,p_rating,currency[0:3],position,brand,market_place,stocks_left])

            
            #time data generation
            ct = datetime.datetime.now()
            data.append([ct,product_url_og,product_name,model_no,price[4:10],discount_perc,soldby,rating,p_rating,currency[0:3],position,brand,market_place])


           
        except:
            print("error occured")
    


df = pd.DataFrame(data, columns=['time', 'product url', 'product name','model no','selling price','discount%','seller','seller raitng','product rating','currency','position','brand','market'])
df.to_csv('noon_web.csv')




 
    
       