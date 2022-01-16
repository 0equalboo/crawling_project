import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=747269&weekday=wed"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons= soup.find_all("td", attrs={"class":"title"}) # class 속성이 title인 모든 "td" element 를 반환
# title = cartoons[1].a.get_text()
# link = cartoons[1].a["href"]
# print(title)
# print(f"https://comic.naver.com{link}") #"문자열" + "문자열" 하면 붙여서 ("문자열", "문자열") 하면 띄어서 출력

# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"] #속성을 가져오려면 대괄호 사용
#     print(title, link) 

cartoons = soup.find_all("div", attrs={"class":"rating_type"})
sum = 0
for cartoon in cartoons: #cartoon = <div class="rating_type"><span class="star"><em style="width:99.61%">평점</em></span><strong>9.96</strong></div> 
    # print(cartoon)
    rank = cartoon.strong.get_text() #cartoon 중 strong element 가져옴 <strong>9.96</strong> 
    #.get_text() = 여는태그와 닫는태그 사이 텍스트 출력
    # = cartoon.find("strong").get_text => cartoon 중 strong element를 찾기
    print(rank) 
    a = float(rank) #변수 a에 <class 'bs4.element.Tag'>를 실수형으로 변환
    
    
    sum = round(sum+a, 2) #평점을 계속해서 sum에 저장
    

rank_average = sum/len(cartoons)
print("총 평점", sum)
print("평균 평점 :", '%.2f' % rank_average) #평점 평균을 소수점 둘째짜리 출력
