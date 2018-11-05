
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


def test():
    print("-------------start------------------")
    object3()
    print("-------------end------------------")

if __name__ == '__main__':
    test()