import math

a=int(input('a를 입력하시오 : ') #입력받은 값은 전부 문자형이므로 앞에 int형을 붙여줘서 변환시킨다.
b=int(input('b를 입력하시오 : ')
c=int(input('c를 입력하시오 : ')
d=b**2-4*a*c
if d>0 :
    x1 = (-b + (b**2-4*a*c)**(1/2)/(2*a)
    x2 = (-b - (b**2-4*a*c)**(1/2)/(2*a)
    print(x1+"또는"+x2) 

if d==0 :
    x = -b / 2 * a

if d<0 :
    x1 = (-b + (b**2-4*a*c)**(1/2)/(2*a)
    x2 = (-b - (b**2-4*a*c)**(1/2)/(2*a)
    print(x1+'또는'+x2)


#          
#x1=-int(b)+int(d)**(1/2)/2*int(a)
#x2=-int(b)-int(d)**(1/2)/2*int(a)
