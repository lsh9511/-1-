"""
문자열의 연산
+ * 
"""
a= "안녕"
b= "하세요"
c= "!"
result = a + b + c
result_10 = result*10
# print(a + b) 
# print(a * 3)  
# print(result)
# print(result*10, sep="  ")
#print(result_10)

import requests
#f 스트링을 이용해서 이강인이라는 값이 들어간 변수를 활용해주세요
# keyword= "이강인"

# url = f"https://m.search.naver.com/search.naver?ssc=tab.m_blog.all&sm=mtb_jum&query={keyword}"

# req = requests.get(url)
# print(req.text)

#keyword ,url 연산자 + 만을 이용해 보세요
# keyword= "이강인"

# url = "https://m.search.naver.com/search.naver?ssc=tab.m_blog.all&sm=mtb_jum&query=" + keyword


# req = requests.get(url)
# print(req.text)

#누가 미리 만들어 놓은 기능 => 내장함수 => input()
keyword= input("검색을 원하는 키워드를 입력해주세요: ")

url = "https://m.search.naver.com/search.naver?ssc=tab.m_blog.all&sm=mtb_jum&query=" + keyword


req = requests.get(url)
print(req.text)

###########input 값을 입력받으면 무조건 데이터타입은 문자형
