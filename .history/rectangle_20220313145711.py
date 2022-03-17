from random import randint
for epoch  in range(100):
num  = 0
    for i in range(3):
        t = randint(0,1)
        num = (num << 1) +  t
    print(num)