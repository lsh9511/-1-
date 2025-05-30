# x = ''

# x += '*/*-*' * 100000


# print(x)

#문자형 -> 이뮤터블 하면서 시퀀스 성격 갖고있다
#시퀀스 : 순서가 있는 자료형에게 부여되는 성격이고 시퀀스 성격을 갖게되면 인덱스를 갖게 됩니다.

# x = 'hello.txt'

# x[5] = '-'
# 문자형은 바꿀수 없다

# x_list = [1,2,3,4,5,6]
# x_list[5] = "안녕"
# print(x_list)
# 리스트는 바꿀수 있다.
# 'hello'
# x[시작 인덱스 : 종료 인덱스]
# x = 'hello.txt'
# print(x[-1:])
#스트라이드 (보폭)
# x[데이터 시작 위치, 데이터 끝 위치, 스트라이드(보폭)]
# x = '-H-E-L-L-O-'
# print(x[1::2])

# x = '토마토'
# x = input("거꾸로 해도 동일한 단어인지 확인하기 : ")
# print (x == x[::-1])

# 내장함수 / 내장 메서드
# print() / 

# x = 'Python'

# print(x.upper())

# file = 'hello.py'

# print(file.replace('py', 'txt'))

# x = 'ababacvada'
# print(x.replace('a', 'A', 10 ))

name = 'Guido van Rossum'

print(name[:5])
print(name.find('Guido'))
