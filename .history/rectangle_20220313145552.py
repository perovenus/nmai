from random import randint


num  = 0
for i in range(3):
    t = randint(0,2)
    num = (num << 1) + randint(0,1)
    print("gia tri cua random"t)
print(num)