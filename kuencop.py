import math

# 근의공식 구하기

a = int(input("a의 값을 입력하세요: ")) #입력받은 값은 전부 문자형이므로 앞에 int형을 붙여줘서 변환시킨다.
b = int(input("b의 값을 입력하세요: "))
c = int(input("c의 값을 입력하세요: "))
d = int(math.pow(b,2)- 4 * a * c)
x1 = ( (-b + d)/2 * a) # -b+제곱근(b**2-4ac/2a)
x2 = ( (-b - d)/2 * a)

if d>0 :
    print("x1 = " , x1)
    print("x2 = " , x2)

elif d==0 :
    print("x = " , x1)

else :
    print("근은 없습니다.")


