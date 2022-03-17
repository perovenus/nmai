from random import randint
num  = 0
for epoch  in range(100):
    for i in range(3):
        t = randint(0,1)
        num = (num << 1) +  t
        print("gia tri cua random",t)
    print(num)