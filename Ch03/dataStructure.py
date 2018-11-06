def object():
    # tuple = 2, 4, 6, 8
    # print(tuple)    # (2, 4, 6, 8)
    tuple1 = tuple([2, 14, 5, 9, 10])
    print(tuple1)    # (2, 14, 5, 9, 10)
    tup = tuple(['foo', [1, 2], True])
    tup[1].append(3)    # 元组中的某个对象是可变的，比如列表
    print(tup)  # ('foo', [1, 2, 3], True)

def object1():
    tup = (4, 5, 6)
    a, b, c = tup
    tup1 = 4, 5, (6, 7)
    a1, b2, (c1, d1) = tup1
    print(c1)

    seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    for a, b, c in seq:
        print(a, b, c)

    values = 1, 2, 3, 4, 5
    a, b, *c = values
    print(a, b, c)

    a = (1, 2, 3, 4, 2, 5, 6, 2, 8, 2)
    print(a.count(2))  # 统计元组里面某个值出现的次数

def object2():
    a = [2, 3, 7, None]
    print(a)
    b = ('Jack', 'Tony', 'Tom')
    print(list(b))  # 元组可以转换成列表
    gen = range(0, 10, 2)
    print(list(gen))

def object3():
    a = [2, 4, 6, 8, 10, 'Jack']
    a.append(12)
    a.insert(1, 10)    # [2, 10, 4, 6, 8, 10, 12]
    a.pop(3)    # [2, 10, 4, 8, 10, 12]
    print(a)
    print('Jack' in a)  # True

def object4():
    a = [4, None, 'foo'] + [7, 8, (2, 3)]
    print(a)
    x = [4, None, 'foo']
    x.extend([7, 8, (2, 3)])    # extend比+效率高
    print(x)

import bisect

def object5():
    a = [9, 5, 1, 6, 8, 19]
    a.sort()
    print(a)

def object6():
    seq = [7, 2, 3, 7, 5, 6, 0, 1]
    print(seq[1:3])
    seq[3:4] = [6, 3]   # [7, 2, 3, 6, 3, 5, 6, 0, 1]
    print(seq)
    print(seq[:3])  # [7, 2, 3]
    print(seq[3:])  # [6, 3, 5, 6, 0, 1]
    print(seq[-3:]) # [6, 0, 1]

def object7():
    a = {'a' : 'some value', 'b' : [1, 2, 3, 4]}
    a['c'] = 'Jack'    # {'a': 'some value', 'b': [1, 2, 3, 4], 'c': 'Jack'}
    #a.pop('a')  # {'b': [1, 2, 3, 4], 'c': 'Jack'}
    print(a)
    b = list(a.keys())
    print(b)
    c = list(a.values())
    print(c)


def test():
    print("-------------start------------------")
    #object1()
    #object2()
    #object3()
    #object4()
    #object5()
    #object6()
    object7()
    print("-------------end------------------")

if __name__ == '__main__':
    test()