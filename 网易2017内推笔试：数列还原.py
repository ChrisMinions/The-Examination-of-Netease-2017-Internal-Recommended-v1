'''
[编程题] 数列还原
时间限制：1秒
空间限制：32768K
牛牛的作业薄上有一个长度为 n 的排列 A，这个排列包含了从1到n的n个数，
但是因为一些原因，其中有一些位置（不超过 10 个）看不清了，
但是牛牛记得这个数列顺序对的数量是 k，顺序对是指满足 i < j 且 A[i] < A[j] 的对数，
请帮助牛牛计算出，符合这个要求的合法排列的数目。 
输入描述:
每个输入包含一个测试用例。每个测试用例的第一行包含两个整数 n 和 k（1 <= n <= 100, 0 <= k <= 1000000000），
接下来的 1 行，包含 n 个数字表示排列 A，其中等于0的项表示看不清的位置（不超过 10 个）。


输出描述:
输出一行表示合法的排列数目。

输入例子1:
5 5
4 0 0 2 0

输出例子1:
2
'''

'''
解题思路：排列组合
  1、根据输入的数列array找出缺失的元素，并把这些元素放入n_arrange中
  2、使用arrangement函数列出n_arrange的所有组合情况，并返回
  3、将n_arrange所有的组合情况分别填入array中，并用count_array函数计算顺序对的数列，若和k相同，返回True，否则返回False
  4、输出所有满足条件的组合数目
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''


def arrangement(array_temp):
    if array_temp:
        array_list = []
        length = len(array_temp)
        for i in range(length):
            temp = array_temp[i:i+1]
            temp_list = arrangement(array_temp[:i]+array_temp[i+1:])
            for each in temp_list:
                array_list.append(temp + each)
        return array_list
    else:
        return [[]]


def count_array(array_temp):
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if array_temp[j] > array_temp[i]:
                count += 1
    if count == k:
        return True
    else:
        return False


def solve():
    n_arrange = list(range(1, n+1))
    for each in array:
        if each in n_arrange:
            n_arrange.remove(each)
    arrangements = arrangement(n_arrange)
    count = 0
    for each in arrangements:
        temp = array[:]
        for j in range(n):
            if temp[j] == 0:
                temp[j] = each.pop()
        if count_array(temp):
            count += 1
    print(count)

n, k = [int(each) for each in input().split()]
array = [int(each) for each in input().split()]
solve()
