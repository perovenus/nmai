from random import randint
num  = 0
f
for i in range(3):
    t = randint(0,1)
    num = (num << 1) +  t
    print("gia tri cua random",t)
print(num)