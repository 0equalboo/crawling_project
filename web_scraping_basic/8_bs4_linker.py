import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=747269&weekday=wed"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons= soup.find_all("td", attrs={"class":"title"})
# title = cartoons[1].a.get_text()
# link = cartoons[1].a["href"]
# print(title)
# print(f"https://comic.naver.com{link}") #문자열 + 문자열 하면 붙여서 문자열, 문자열 하면 띄어서

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"] #속성을 가져오려면 대괄호 사용
    print(title, link)