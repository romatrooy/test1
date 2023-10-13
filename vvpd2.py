'''vvpd3'''
def menu():
    '''program menu'''
    print('1 --> first task \n2 --> second task \n3 --> third task \n stop --> finish program')

def func1(a:list, b:list):
    '''first task'''
    res_1 = []
    for i in a:
        if a.count(i) == 1 and b.count(i) > 1:
            res_1.append(i)
    return res_1

def func2(a:list, b:list):
    '''second task'''
    res_2 = []
    for j in a:
        if b.count(j) == 0:
            res_2.append(j)
    return res_2

