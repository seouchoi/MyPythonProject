import requests
from bs4 import BeautifulSoup

url = "https://nadocoding.tistory.com/"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()

with open("nadocoding.html","w",encoding="utf8") as f:
    f.write(res.text)

soup = BeautifulSoup(res.text, "lxml")
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a) #soup 객체에서 처음 발견되는 a element 출력
#print(soup.a.attrs) #a element 의 속성 정보를 출력
#print(soup.a["href"]) #a element 의 href 속성 '값'정보를 출력

#print(soup.find(attrs={"class":"tit_post"}))
content = soup.find(attrs={"class":"thumbnail_post"})
print(content.next_sibling.next_sibling)

