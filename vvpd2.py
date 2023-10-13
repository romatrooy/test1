'''vvpd3'''
def menu():
    '''program menu'''
    print('1 --> first task \n2 --> second task \n3 --> third task \nstop --> finish program')

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

def func3(a:list, b:list):
    '''fird task'''
    res_3 = []
    for l in a:
        if a.count(l) == b.count(l) == 1:
            res_3.append(l)
    return res_3

F = ''
while F != "stop":
    menu()
    F = str(input())
    if F == 'stop':
        print('program finished')
        break
    try:
        a = list(map(int, input().split(',')))
    except ValueError:
        print('not all values in list "a" are integers'
              'enter "a" again')
        try:
            a = list(map(int, input().split(',')))
        except ValueError:
            print('program break')
            break
    try:
        b = list(map(int, input().split(',')))
    except ValueError:
        print('not all values in list "b" are integers'
              'enter "b" again')
        try:
            b = list(map(int, input().split(',')))
        except ValueError:
            print('program break')
            break
    if F == '1':
        print(func1(a, b))
    elif F == '2':
        print(func2(a, b))
    elif F == '3':
        print(func3(a, b))
