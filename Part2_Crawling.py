import requests
from bs4 import BeautifulSoup
# coding=utf-8

re = requests.get('https://www.ptt.cc/bbs/HatePolitics/index.html')

soup = BeautifulSoup(re.text, "html.parser")

for line in soup.select('.r-ent'):
    print(line.select('.date')[0].text)
    print(line.select('.author')[0].text)
    print(line.select('.title')[0].text)