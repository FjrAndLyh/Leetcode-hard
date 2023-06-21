"""
动态规划DP,dfs深度优先搜索，bfs广度优先搜索------一道题弄懂
题目描述:
在一个mxn的矩阵中，从左上角走到右下角，有多少种路径?只能向左或者向右
输出路径总数
"""
"""
例子在这里:
"""
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0],[0,0,0],[0,0,0],[0,0,1]]
maxrow = 6 - 1
maxcol = 3 - 1
#leetcode 不同路径 总数
#给定grid数组，查找从左上角走到右下角的路径总数和
#只能向下走或者向右走
#入栈(并且更新栈顶)
def instack(stack,data,top):
    stack.append(data)
    top += 1
    return top
#出栈(并且更新栈顶)
def outstack(stack,top,xy):
    xy = stack[top]
    del stack[top]
    top -= 1
    return top
#最终解决的代码:
def dfs_solution():
    # 建立一个栈
    stack = []
    #先将起点存入栈中
    top = -1
    top = instack(stack,[0,0],top)
    #xy用于接收栈中的元素坐标
    xy = [0,0]
    #num是总次数
    num = 0
    #循环直到栈空
    while(len(stack)!=0):
        #取出栈顶元素
        xy = stack[top]
        top = outstack(stack,top,xy)
        #检测可行走的两个点放入栈中
        row = xy[0]
        col = xy[1]
        #如果是终点，那么路径数就+1,路径总数实际上就是到达终点的次数
        if grid[row][col]==1:
            num += 1
        if row+1<=maxrow:
            top = instack(stack,[row+1,col],top)
        if col+1<=maxcol:
            top = instack(stack,[row,col+1],top)
    print(num)
"""
以上是经典的dfs的做法，直接遍历搜索了整颗树
下面我们来看经典的bfs，广度优先搜索怎么做
"""
#入队
def cinq(q,data):
    q.append(data)
#出队
def outq(q):
    del q[0]
#解决代码
def bfs_solution():
    # 建立一个队列
    q = []
    #先放起点进入队列
    q.append([0,0])
    num = 0
    #循环直到队空
    while(len(q)!=0):
        #取出队列元素
        xy = q[0]
        row = xy[0]
        col = xy[1]
        outq(q)
        # 如果是终点，那么路径数就+1,路径总数实际上就是到达终点的次数
        if grid[row][col] == 1:
            num += 1
        if row + 1 <= maxrow:
            cinq(q,[row+1,col])
        if col + 1 <= maxcol:
            cinq(q,[row,col+1])
    print(num)
"""
看完bfs,dfs直接弄懂深搜，广搜
下面使用动态规划DP解决
构建dp数组，理清dp数组的含义
"""
def dp_solution():
    #构建dp数组，并且赋予dp数组含义,并且初始化dp数组
    dp = [[0,0,0,],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    num = 0
    """
    我们发现我们想要走到的终点坐标是[maxrow,maxcol]
    那么我们走到这一点前，需要先走到[maxrow-1,maxcol]和[maxrow,maxcol-1]的位置
    而我们走到这两点时，只需要一步就能走到终点
    问题转换为 走到[maxrow-1,maxcol]有多少种走法?
    走到[maxrow,maxcol-1]有多少种走法?
    我们假设dp[row][col]的值等于走到坐标[row,col]的点的路径数
    那么，我们得出递推式:↓
    dp[row][col] = dp[row-1][col] + dp[row][col-1]
    所以，想要得到dp[maxrow,maxcol],就必须遍历bp[i][j]每一个格子的值
    """
    #我们使用循环遍历dp数组，最后输出dp[maxr,maxc]
    #我们首先发现，在第一列上的所有点，和一行的所有点,都只有一种到达的方式
    #所以遍历这些点，赋值1
    i = 0
    while(i<=maxrow):
        dp[i][0]=1
        i += 1
    i = 0
    while (i <= maxcol):
        dp[0][i] = 1
        i += 1
    #第一个点到达的路径没有，所以赋值0
    dp[0][0] = 0
    #遍历整个bp数组，直到求出dp[maxrow][maxcol]
    #刚刚遍历过两列了,那么将延后开始遍历
    i = 1
    j = 1
    while(i<=maxrow):
        while(j<=maxcol):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            j += 1
        j = 0
        i += 1
    print(dp[maxrow][maxcol])
    print(dp)

if __name__ == '__main__':
    dfs_solution()
    bfs_solution()
    dp_solution()