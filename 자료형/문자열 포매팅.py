# 1. 숫자 바로 대입

a = "I eat %d apples." % 3

print(a)


# 2. 문자열 바로 대입

b = "I eat %s apples." %"five"
print(b)

# 3. 숫자 값을 나타내는 변수로 대입

number = 6
c = "I eat %d apples." % number
print (c)

# 4. 2개 이상의 값 넣기

number = 10
day = "three"
d = "I ate %d apples. so I was sick for %s days." % (number, day)
print(d)



"""  
문자열 포맷코드

코드	설명
%s	문자열(String)
%c	문자 1개(character)
%d	정수(Integer)
%f	부동소수(floating-point)
%o	8진수
%x	16진수
%%	Literal % (문자 % 자체)

"""