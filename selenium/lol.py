from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import requests
from bs4 import BeautifulSoup
from flask import request

username = input("Enter a user to search for : ")
# url = "https://google.com"
url = "http://fow.kr/find/"+ username

# req = request(url, headers={'User-Agent' : 'Mozilla/5.0'})
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
# res = requests.get(url, headers=req) 
# page = urlopen(req).read()

res =  requests.get(url)
res.raise_for_status()



# from urllib.request import Request, urlopen
# req = Request('http://www.cmegroup.com/trading/products/#sortField=oi&sortAsc=false&venues=3&page=1&cleared=1&group=1', headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
# res = requests.get(url, headers=headers) 
# print("응답코드 :", res.status_code)
# with open("kwonbo.html", "w", encoding="utf8") as f:
# f.write(res.text)



soup = BeautifulSoup(res.text, 'lxml')

#/html/body/div[5]/div[1]/div[1]/div[6]/div[1]/div[2]/b/font
games = soup.find_all("div", attrs={"class":"table_summary"})

for game in games:
    rank = str(game.get_text())
rank_1 = rank.split()

number = 0
printf = f"\n{username}의 league of legend 전적\n"

for i in rank_1:
    if number == 0:
        print(printf.center(100, '-'))
    print(i,end=" ")
    number+=1
    if "%)" in i:
        print("\n")
    if i == ")":
        if number == 4:
            print("\n")
    
    if "0전" in rank_1:
        if "0패" in i:
            print("\n")
        

   
    # rank_1 = rank.replace("\n","")
    
# rank = games.b.get_text()
# print(rank)

# games = soup.find_all("span", attrs={"class":"tipsy_live"})
# for game in games:
#     print(game.get_text())



# driver = webdriver.Chrome()
# driver.get("https://www.op.gg/")

# elem = driver.find_element_by_name("searchUserName")
# elem.send_keys("google") #크롤링 대상 (가져올 이미지) 선택
# elem.send_keys(Keys.RETURN) #엔터키
# for i in range(0, 5):
#     driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[i+1].click() #i번째 이미지 클릭
#     time.sleep(3) #사진 로딩 시간
#     imageUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src") #이미지 주소 찾기
#     opener=urllib.request.build_opener()
#     opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
#     urllib.request.install_opener(opener)
#     urllib.request.urlretrieve(imageUrl, f"test{i}.jpg") #testi.jpg로 저장
#selenium을 통한 크롬 이미지 크롤링