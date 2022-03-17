from random import randint


num  = 0
for i in range(3):
    num = num << 1 + randint(0,1)
print(num)