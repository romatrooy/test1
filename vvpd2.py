'''vvpd3'''
from random import randint

a = [randint(1, 100) for i in range(100)]
b = [randint(1, 100) for j in range(100)]

def func1(a:list, b:list):
    res_1 = []
    for i in a:
        if a.count(i) == 1 and b.count(i) > 1:
            res_1.append(i)
    return res_1
def func2(a:list, b:list):
    res_2 = []
    for j in a:
        if b.count(j) == 0:
            res_2.append(j)
    return res_2
def func3(a:list, b:list):
    res_3 = []
    for l in a:
        if a.count(l) == b.count(l) == 1:
            res_3.append(l)
    return res_3
print(func1(a,b))
print(func2(a,b))
print(func3(a,b))