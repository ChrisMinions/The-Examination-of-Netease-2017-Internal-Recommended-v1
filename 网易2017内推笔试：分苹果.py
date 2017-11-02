'''
[编程题] 分苹果
时间限制：1秒
空间限制：32768K
n 只奶牛坐在一排，每个奶牛拥有 ai 个苹果，现在你要在它们之间转移苹果，
使得最后所有奶牛拥有的苹果数都相同，每一次，你只能从一只奶牛身上拿走恰好两个苹果到另一个奶牛上，
问最少需要移动多少次可以平分苹果，如果方案不存在输出 -1。 
输入描述:
每个输入包含一个测试用例。每个测试用例的第一行包含一个整数 n（1 <= n <= 100），
接下来的一行包含 n 个整数 ai（1 <= ai <= 100）。


输出描述:
输出一行表示最少需要移动多少次可以平分苹果，如果方案不存在则输出 -1。

输入例子1:
4
7 15 9 5

输出例子1:
3
'''

'''
解题思路：仔细小心
  这道题的解题思路不难，看代码应该可以理解，小心仔细，别犯一下粗心错误就行
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

n = int(input())
a_n = [int(each) for each in input().split()]

if sum(a_n) % n != 0:
    print(-1)
else:
    max_apple = max(a_n)
    min_apple = min(a_n)
    count = 0
    while max_apple - min_apple > 2:
        a_n[a_n.index(max_apple)] = max_apple - 2
        a_n[a_n.index(min_apple)] = min_apple + 2
        max_apple = max(a_n)
        min_apple = min(a_n)
        count += 1

    if a_n.count(a_n[0]) == n:
        print(count)
    else:
        print(-1)
