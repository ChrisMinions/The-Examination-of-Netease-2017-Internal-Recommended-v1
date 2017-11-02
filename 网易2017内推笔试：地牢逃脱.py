'''
[编程题] 地牢逃脱
时间限制：1秒
空间限制：32768K
给定一个 n 行 m 列的地牢，其中 '.' 表示可以通行的位置，'X' 表示不可通行的障碍，
牛牛从 (x0 , y0 ) 位置出发，遍历这个地牢，和一般的游戏所不同的是，他每一步只能按照一些指定的步长遍历地牢，
要求每一步都不可以超过地牢的边界，也不能到达障碍上。地牢的出口可能在任意某个可以通行的位置上。
牛牛想知道最坏情况下，他需要多少步才可以离开这个地牢。 
输入描述:
每个输入包含 1 个测试用例。每个测试用例的第一行包含两个整数 n 和 m（1 <= n, m <= 50），表示地牢的长和宽。
接下来的 n 行，每行 m 个字符，描述地牢，地牢将至少包含两个 '.'。
接下来的一行，包含两个整数 x0, y0，表示牛牛的出发位置
（0 <= x0 < n, 0 <= y0 < m，左上角的坐标为 （0, 0），出发位置一定是 '.'）。
之后的一行包含一个整数 k（0 < k <= 50）表示牛牛合法的步长数，
接下来的 k 行，每行两个整数 dx, dy 表示每次可选择移动的行和列步长（-50 <= dx, dy <= 50）


输出描述:
输出一行一个数字表示最坏情况下需要多少次移动可以离开地牢，如果永远无法离开，输出 -1。
以下测试用例中，牛牛可以上下左右移动，在所有可通行的位置.上，地牢出口如果被设置在右下角，
牛牛想离开需要移动的次数最多，为3次。

输入例子1:
3 3
...
...
...
0 1
4
1 0
0 1
-1 0
0 -1

输出例子1:
3
'''

'''
解题思路：广度优先搜索算法（bfs）
  这题的题目描述给差评，读了好几遍才读懂一点，它的意思应该是步长给定，牛牛以最小的步数达到所有非障碍的点，
  输出花费最多的步长数量，如果有达到不了的点，直接输出-1
  1、用search函数搜索牛牛到达非障碍点的步数，searched存储已经搜索过的点
  2、在search函数中，先遍历判断当前点列表中所有点，看是否有于目标点重合的点，若有返回0，
  否则将该点放入searched中，并用explore函数探索从该点经过指定步长能到达的点，返回能到达且不是障碍未被搜索过的点
  3、将explore返回的点集放入wait_search_set中，表示待搜索的点，如果它为空，表示已经没有待搜索的点了，搜索失败，返回-1
  若它非空，则用它递归search，如果递归返回-1，该层search也返回-1，否则返回 1+递归search返回值 表示步数
'''

'''
代码运行结果：
运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
case通过率为90.00%
'''


n, m = [int(each) for each in input().split()]
MAP = []
for i in range(n):
    MAP.append([each for each in input()])
INIT_POS = tuple([int(each) for each in input().split()])
k = int(input())
STEPS = []
for i in range(k):
    STEPS.append([int(each) for each in input().split()])


def explore(pos):
    reachable_neighbor = set()
    for j in range(k):
        temp_row = pos[0] + STEPS[j][0]
        temp_column = pos[1] + STEPS[j][1]
        if 0 <= temp_row < n and 0 <= temp_column < m:
            if MAP[temp_row][temp_column] != 'X' and (temp_row, temp_column) not in searched:
                reachable_neighbor.add((temp_row, temp_column))
    return reachable_neighbor


def search(current_pos_set, target):
    wait_search_set = set()
    for each_pos in current_pos_set:
        if each_pos == target:
            return 0
        else:
            searched.add(each_pos)
            wait_search_set.update(explore(each_pos))
    if wait_search_set:
        steps = search(wait_search_set, target)
        if steps != -1:
            return 1 + steps
        else:
            return -1
    else:
        return -1

max_steps = -1
init_set = set()
init_set.add(INIT_POS)

for row in range(n):
    for column in range(m):
        searched = set()
        if MAP[row][column] != 'X' and (row, column) != INIT_POS:
            step = search(set(init_set), (row, column))
            if step == -1:
                max_steps = -1
                break
            elif step > max_steps:
                max_steps = step

print(max_steps)
