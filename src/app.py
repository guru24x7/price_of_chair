import requests
from bs4 import BeautifulSoup

# this is comment

request = requests.get("http://www.officedepot.com/a/products/510830/WorkPro-Quantum-9000-Series-Ergonomic-Mesh/")
content = request.content
# <span class="pricing_format fleft" data-auid="productDetail_value_itemPrice0">289</span>
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "pricing_format fleft", "data-auid": "productDetail_value_itemPrice0"})
string_price = element.text.strip()
price_without_symbol = int(string_price[0:])

if price_without_symbol < 290:
    print("You should buy the chair")
    print("The current price is {} ".format(string_price))
else:
    print("Do not buy, its to costly")









