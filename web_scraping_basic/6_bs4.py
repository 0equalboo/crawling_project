import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) 처음으로 발견되는 a 엘리먼트 출력
# print(soup.a.attrs) a 앨리먼트의 속성정보 출력
# print(soup.a["onclick"]) #a 앨리먼트의 onclick 속성 '값(value)' 정보를 출력

# print(soup.find("a", attrs={"Nbtn_upload"})) #a 태그의 해당하는 앨리먼트 중 class 의 속성이 'Nbtn_upload'인 처음으로 발견되는 element
# print(soup.find(attrs={"Nbtn_upload"})) #class="Nbtn_upload"인 element 탐색

# print(soup.find("li", attrs={"class":"rank01"}))

# rank1 = soup.find("li", attrs={"class":"rank01"})

# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li")) 

webtoon = soup.find("a", text="존망코인-10화 이게 사치가 아니면 뭐임!")
print(webtoon)