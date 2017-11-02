'''
[编程题] 合唱团
时间限制：1秒
空间限制：32768K
有 n 个学生站成一排，每个学生有一个能力值，牛牛想从这 n 个学生中按照顺序选取 k 名学生，
要求相邻两个学生的位置编号的差不超过 d，使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？ 
输入描述:
每个输入包含 1 个测试用例。每个测试数据的第一行包含一个整数 n (1 <= n <= 50)，表示学生的个数，
接下来的一行，包含 n 个整数，按顺序表示每个学生的能力值 ai（-50 <= ai <= 50）。
接下来的一行包含两个整数，k 和 d (1 <= k <= 10, 1 <= d <= 50)。


输出描述:
输出一行表示最大的乘积。

输入例子1:
3
7 4 7
2 50

输出例子1:
49
'''

'''
解题思路：三重循环嵌套 + 动态规划
  第一重循环：对学生数量从1到k进行循环，用i表示学生数量，
  循环一次得到i个学生以各个编号结尾的最大或最小乘积（因为可能存在负数），保存在dp中
  第二重循环：对i个学生中的最大编号从i到N进行循环，用j表示最大编号，循环选取新的编号最大的同学
  第三重循环：对以编号j-d到j结尾同学们的最大和者最小乘积进行循环，并将乘积都乘以第j位同学的能力，
  选取新的最大最小乘积，并用该乘积更新dp
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''


N = int(input())
abilities = [int(each) for each in input().split()]
k, d = [int(each) for each in input().split()]

dp = [(each, each) for each in abilities]

for i in range(1, k):
    dp_ = dp[:i]
    for j in range(i, N):
        temp_list = []
        for z in range(j-d, j):
            if z < 0:
                continue
            else:
                temp_list.append(abilities[j]*dp[z][0])
                temp_list.append(abilities[j]*dp[z][1])
        dp_.append((max(temp_list), min(temp_list)))
    dp = dp_

print(max([max(each) for each in dp]))
