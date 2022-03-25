#1. 30이상 출력#

for x in data :
    if x >=30 :
        print(x,end=' ')
print('done')

#2. 40보다 크고 50 미만 출력(and)
for y in data :
    if y > 40 and y < 50 :
        print(y,end=' ')
print('done')
#3. 20보다 작거나 50이상 출력(or)
for z in data :
    if z < 20 or z >=50 :
        print(z,end=',')
print('done')        
#4. 홀수값 출력
for a in data :
    if a%2==1 :
        print(a,end='ㅣ')
print('done')
#5. 30이상 갯수
howmany = 0
for b in data :
    if b >= 30 :
        howmany=howmany+1
print(howmany)
