import requests
from bs4 import BeautifulSoup

url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#티스토리 전체 목록 가져오기 
blogLists = soup.find_all("a",attrs = {"class":"link_sub_item"})
#class속성이 link_sub_item인 모든 "a" element반환
for blogList in blogLists:
    print(blogList.get_text()) 