import requests
from bs4 import BeautifulSoup
url="https://finance.naver.com/sise/"
request=requests.get(url).text
soup=BeautifulSoup(request,"html.parser") 

now_value=soup.select_one("#KOSPI_now").text
a=soup.find("span",{"id":"KOSPI_now"}).text
print(f"현재 코스피 지수:{now_value}")
print(a)