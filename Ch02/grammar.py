
def object1():
    a = [1, 2, 3]
    b = a   # a和b是同一个对象，对同一个对象的双重引用
    print(b)
    print(a == b)   # True
    print(a is b)   # True
    a.append(4)
    print(b)    # [1, 2, 3, 4]

def object2():
    a = [1, 2, 3]
    b = list(a) # 会创建一个新的列表
    print(b)
    print(a == b)   # True
    print(a is b)   # False
    print(a is not b)  # False
    a.append(4)
    print(b)    # [1, 2, 3]

def object3():
    a_list = ['aaa', 1, [2, 6]]
    a_list[1] = 'ccc'   # 列表、字典、NumPy数组，和用户定义的类 这些对象或包含的值可以被修改
    print(a_list)
    b_tuple = ('aaa', 1, [2, 6])    # 字符串和元组  这些对象或包含的值不可以被修改
    b_tuple[2][1] = 5   # 但是元组里面的列表的值是可以修改的
    print(b_tuple)

def object4():
    a = 'Python'
    b = list(a)
    print(b[:3])    # ['P', 'y', 't']
    print(b[3:])    # ['h', 'o', 'n']
    s = '12\\34'    # 12\34
    print(s)
    l = r'this\has\no\special\characters'   # this\has\no\special\characters
    print(l)
    c = 'this is the first half '
    d = 'and this is the second half'
    print(c + d)    # this is the first half and this is the second half

def object5():
    a = None
    print(a is None)   # True
    b = 5
    print(b is not None)  # True

def object6():
    x = 3
    if x < 0:
        print()
    elif x == 0:
        print('Equal to zero')
    elif 0 < x < 5:
        print('Positive but smaller than 5')
    else:
        print('Positive and larger than or equal to 5')

def object7():
    a_list = [3, 7, 8, 4, 5]
    for i in a_list:
        print(i)

    x = 256
    total = 0
    while x > 0:
        if total > 500:
            break
        total += x
        x = x // 2
    print(total)    # 504

    for i in range(5):
        print(i)

    print(list(range(0, 20, 2)))    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    print(list(range(5, 0, -1)))    # [5, 4, 3, 2, 1]



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