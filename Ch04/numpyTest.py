import numpy as np

import numpy as np

# data = np.random.randn(2, 3, 4)
# data1 = np.random.randn(3, 2)
#
# print(data)
# print(data1)

# list = [[1, 2, 3, 8], [2, 3, 8 , 9]]
# np_arr = np.array(list)
# print(np.shape(np_arr))

# list = [2.2, 4.1, 6.444, 8.891]
# np_arr = np.array(list, dtype=np.int)
# #
# # np_arr = np_arr.astype(np.float) # 注意该处的赋值
# print(np_arr.astype(np.int32))

# arr1 = np.array([[1., 2., 3.],
# #                  [4., 5., 6.]])
# # arr2 = np.array([[1., 2., 3.],
# #                  [1., 2., 3.]])
# # print(arr1.dtype)
# # print(arr1 * arr2)


# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
# # arr[1, 1] arr[1][1] 两者等价
# print(arr[1, 1])
#
# # 切片 两者不等价
# print(arr[:2, 1:])
# #[[2 3]
# #[5 6]]
# print(arr[:2][1:])
# #[[4 5 6]]

# arr = np.empty((8, 4))
# for i in range(8):
#     arr[i] = i+10
# print(arr)
# print(arr[0])
#
# # 转置
# arr = np.arange(15).reshape((3, 5))
# print(arr)
# print(arr.T)


# #np.dot计算矩阵内积
# np_arr1 = np.array([[1, 2, 3, 8], [2, 3, 8 , 9]])
# np_arr2 = np.array([[1, 2], [3, 8], [2, 3], [8 , 9]])
# print(np.dot(np_arr1, np_arr2))

# # 对这些轴进行转置
# arr = np.arange(16).reshape((2, 2, 4))
# print(arr)
# print(arr.transpose((1, 0, 2)))

arr = np.random.randn(5, 4)
print(arr)
print(arr.sum())

# arr.max()
# arr.min()
# arr.mean()
# arr[1].mean() 某一行
# arr.sum()

# arr.sum(axis=0)
# arr.mean(1)是“计算行的平均值”，arr.sum(0)是“计算每列的和”
print(arr.sum(axis=0))
print(arr.sum(0))


def object():
    print()

def test():
    print("-------------start------------------")
    print("-------------end------------------")

if __name__ == '__main__':
    test()