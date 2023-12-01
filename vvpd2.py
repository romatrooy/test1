'''vvpd3'''
def menu():
    '''program menu'''
    print('1 --> first task \n2 --> second task \n3 --> third task \nstop --> finish program')

def enter():
    '''infiniyt enter'''
    lst = list(input().split(','))
    flg = lst[0]
    try:
        lst = list(map(int, lst))
        return lst
    except ValueError:
        if flg == 'stop':
            return 'stop'
        print('Try again')
        return enter()

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

# удалил 2 функции
# сделал форк проекта и назвал его friend
# создам один коммит
# запушу


if __name__ == '__main__':
    F = ''
    while F != "stop":
        menu()
        F = str(input())
        if F == 'stop':
            print('program finished')
            break
        try:
            print('enter a')
            a = list(input().split(','))
            if a[0] == 'stop':
                print('program finished')
                break
            a = list(map(int, a))
        except ValueError:
            print('not all values in list "a" are integers'
                  ' enter "a" again')
            a = enter()
            if a == 'stop':
                print('program finished')
                break
        try:
            print('enter b')
            b = list(input().split(','))
            if b[0] == 'stop':
                print('program finished')
                break
            b = list(map(int, b))
        except ValueError:
            print('not all values in list "a" are integers'
                  ' enter "a" again')
            b = enter()
            if b == 'stop':
                print('program finished')
                break
        if F == '1':
            print(func1(a, b))
        elif F == '2':
            print(func2(a, b))
        elif F == '3':
            print(func3(a, b))
#test 
