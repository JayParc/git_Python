"""
n=5
while n > 0 :
    print(n)
    n=n-1
print('발사')
"""

"""
import time
n=5
while n > 0 :
    time.sleep(1) #1초 시간 지연
    print(n)
    n=n-1
print('발사')
"""
"""
import time
n=0
while n < 5 :
    time.sleep(1)
    print(n)
    n=n+1
print('끝')
"""
"""
n=5
while n > 0 :
    print(n)
    n=n-1
print('발사')
"""
"""
import time
n=5
while n > 0:
    time.sleep(1)
    print(n)
    n=n-1
print('발사')
"""
"""
n=0
while True :
    n=n+1
    print(n)
    if n > 5 :
        break
print('끝')
"""
'''
data = [32,14,55,23,12,67,44]
for JJak in data :
    if JJak % 2 == 0:
        print(JJak)
print('끝')
'''
"""
n= 0;
while True :
    if n>10 :
        break;
    n=n+1
    print(n,end=' ')
    print('아니오')

print('끝')
print(n)
"""
"""
friends = ['Joseph', 'Glenn', 'Sally']
for k in friends :
    print(k)
"""
'''
data = [32,14,55,12,67,44]
for x in data :
    # print(x,end=' ')
    if x>40 and x<=55 :
        print(x,end=',')
print('끝')        
'''
data = [32,14,55,12,67,80,9,27,44,39,30]

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
