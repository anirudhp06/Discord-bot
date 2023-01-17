import requests
import sys
from bs4 import BeautifulSoup as bs
res=requests.get("https://cetonline.karnataka.gov.in/kea/Pgcet22",verify=False)
soup=bs(res.text,features="html.parser")
doc=soup.find(id="ContentPlaceHolder1_req_accordion")
print(len(doc))