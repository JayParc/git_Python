import math

# 근의공식 구하기

a = int(input("a의 값을 입력하세요: ")) #입력받은 값은 전부 문자형이므로 앞에 int형을 붙여줘서 변환시킨다.
b = int(input("b의 값을 입력하세요: ")) 
c = int(input("c의 값을 입력하세요: "))
d = int(math.pow(b,2)- 4 * a * c)
x1 = ( (-b + d**0.5))/(2 * a) # -b+제곱근(b**2-4ac/2a) 혹은 -b+제곱근 (b**2-4ac/2a)
x2 = ( (-b - d**0.5))/(2 * a)

if d>0 :
    print("x1 = " , x1)
    print('또는')
    print("x2 = " , x2)

elif d==0 :
    print("x = " , x1) # 근은 한개이다. 

else :
    print("허근입니다.") #루트 -1은 i이기에 허수이다.


