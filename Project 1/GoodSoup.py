from bs4 import BeautifulSoup
import requests

url= "https://www.newegg.com/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

print(doc.prettify)

