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



def test():
    print("-------------start------------------")
    #object1()
    object2()
    print("-------------end------------------")

if __name__ == '__main__':
    test()