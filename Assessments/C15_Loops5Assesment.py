'''
Write a program from 1 to 50
>>> but skip numbers divisable by 5
>>> stop completely if it reaches 40'''


n = 0    
while True:
    n +=1
    if (n == 40):
        break
    if(n % 5 == 0):
        continue
    print(n)

for i in range(1,51):
    if i == 40:
        break
    elif i % 5 == 0:
        continue
    else:
        print(i)