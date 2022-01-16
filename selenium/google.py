from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")

elem = driver.find_element_by_name("q")
elem.send_keys("랄로") #크롤링 대상 (가져올 이미지) 선택
elem.send_keys(Keys.RETURN) #엔터키
for i in range(0, 5):
    driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[i+1].click() #i번째 이미지 클릭
    time.sleep(3) #사진 로딩 시간
    imageUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src") #이미지 주소 찾기
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(imageUrl, f"test{i}.jpg") #testi.jpg로 저장
#selenium을 통한 크롬 이미지 크롤링