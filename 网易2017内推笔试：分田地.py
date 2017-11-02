'''
[编程题] 分田地
时间限制：1秒
空间限制：32768K
牛牛和 15 个朋友来玩打土豪分田地的游戏，牛牛决定让你来分田地，地主的田地可以看成是一个矩形，每个位置有一个价值。
分割田地的方法是横竖各切三刀，分成 16 份，作为领导干部，牛牛总是会选择其中总价值最小的一份田地， 
作为牛牛最好的朋友，你希望牛牛取得的田地的价值和尽可能大，你知道这个值最大可以是多少吗？ 
输入描述:
每个输入包含 1 个测试用例。每个测试用例的第一行包含两个整数 n 和 m（1 <= n, m <= 75），
表示田地的大小，接下来的 n 行，每行包含 m 个 0-9 之间的数字，表示每块位置的价值。


输出描述:
输出一行表示牛牛所能取得的最大的价值。

输入例子1:
4 4
3332
3233
3332
2323

输出例子1:
2
'''

'''
解题思路：二分法寻优 + 四重循环嵌套
  用二分法找出比16份土地价值都小的那个最大的数
  一开始mid取为所有土地价值和的一半，使用这个mid在judge函数中进行四重循环嵌套：
    前三重循环遍历任意一种竖切的方案
    我们现在土地的最上方切一刀，然后用第四重循环遍历土地的行数去寻找下一刀的位置
    如果当前行之前一刀所在行和竖着三刀所在行构成的四个区域，每一个区域的价值和都大于mid，则在此处切一刀，接着继续寻找下一刀
    第四重循环结束后，若判断  刀数是否大于等于4，若是，返回True，否则返回False
  利用judge的返回值获取新的二分值，直至满足停止条件位置，二分法的细节不过多赘述
tips：
  计算各块土地价值时用了一些小技巧，可以极大加快计算效率，但尽管如此，受限于python糟糕的运行效率，代码的AC率只有10%，
  强烈建议下次笔试时可以使用numpy
'''

'''
代码运行结果：
运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
case通过率为10.00%
'''

n, m = [int(each) for each in input().split()]
field = []
for each in range(n):
    field.append([int(each) for each in input()])

sum_array = [[0]*(m+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        sum_array[i][j] = sum_array[i][j-1] + sum_array[i-1][j] - sum_array[i-1][j-1] + field[i-1][j-1]


def judge(mid):
    def calc_sum(x1, x2, y1, y2):
        return sum_array[x2][y2] - sum_array[x2][y1] - sum_array[x1][y2] + sum_array[x1][y1]
    for x in range(1, m-2):
        for y in range(x+1, m-1):
            for z in range(y+1, m):
                row_count = 0
                prev_row = 0
                for r in range(1, n):
                    if calc_sum(prev_row, r, 0, x) >= mid and calc_sum(prev_row, r, x, y) >= mid and \
                       calc_sum(prev_row, r, y, z) >= mid and calc_sum(prev_row, r, z, m) >= mid:
                        row_count += 1
                        prev_row = r
                if row_count >= 3:
                    return True
    return False

left = 0
right = sum_array[n][m]
while left <= right:
    anchor = (left + right) // 2
    if judge(anchor):
        left = anchor + 1
        answer = anchor
    else:
        right = anchor - 1

print(anchor)
