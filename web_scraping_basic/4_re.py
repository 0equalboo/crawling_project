import re
#ca?e
#caae, cabe, cace, cade...
p = re.compile("ca.e") #정규식 기본
# . (ca.e) : 하나의 문자를 의미 > care, cafe, caae.. != caffe
# ^ (^de)  : 문자열의 시작을 의미 > desk, destination, delight... != collect
# $ (se$)  : 문자열의 끝을 의미 > case, base, choose... != face


#print(m.group()) # 매치되지 않으면 에러 발생
def print_match(m):
    if m:
        print("m.group() : ", m.group()) #일치하는 문자열 반환
        print("m.string : ", m.string) #입력받은 문자열 반환
        print("m.start() :", m.start()) #일치하는 문자열의 시작인덱스를 반환
        print("m.end() :", m.end()) # 일치하는 문자열의 끝인덱스를 반환
        print("m.span() :", m.span()) #일치하는 문자열의 시작과 끝 인덱스를 반환
    else:
        print("매칭되지 않음")

# m = p.match("careless") #match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care") #search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# m = p.findall("care cafe") #findall : 일치하는 모든 것을 리스트 형태로 반환
# print(m)

# 1. p = re.compile("원하는 형태") : 원하는 형태로 compile(p라는 변수로 받음)
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 list형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cafe, caae.. != caffe
# ^ (^de)  : 문자열의 시작을 의미 > desk, destination, delight... != collect
# $ (se$)  : 문자열의 끝을 의미 > case, base, choose... != face