from random import randint

from pyrsistent import T


num  = 0
for i in range(3):
    t = randint(0,1)
    num = (num << 1) +  t
    print("gia tri cua random",t)
print(num)