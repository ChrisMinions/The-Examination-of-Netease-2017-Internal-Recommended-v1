'''
[编程题] 藏宝图
时间限制：1秒
空间限制：32768K
牛牛拿到了一个藏宝图，顺着藏宝图的指示，牛牛发现了一个藏宝盒，藏宝盒上有一个机关，
机关每次会显示两个字符串 s 和 t，根据古老的传说，牛牛需要每次都回答 t 是否是 s 的子序列。
注意，子序列不要求在原字符串中是连续的，例如串 abc，它的子序列就有 {空串, a, b, c, ab, ac, bc, abc} 8 种。 
输入描述:
每个输入包含一个测试用例。每个测试用例包含两行长度不超过 10 的不包含空格的可见 ASCII 字符串。


输出描述:
输出一行 “Yes” 或者 “No” 表示结果。

输入例子1:
x.nowcoder.com
ooo

输出例子1:
Yes
'''

'''
解题思路：不必使用动态规划
  此题不需要求最长公共子序列的长度，只需要判断是否是子序列即可，因此不必使用动态规划，利用循环进行简单的判断即可
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

s = input()
t = input()
length = len(t)
i = 0
for each in s:
    if i == length:
        break
    if each == t[i]:
        i += 1

if i == length:
    print('Yes')
else:
    print('No')
