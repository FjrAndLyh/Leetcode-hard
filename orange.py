'''
一题弄懂 bfs 广搜
'''
#实现一个队列
#入队
def comin(q,data):
    '''
    :param q:队列
    :param top: 队列最高位指针
    :param data: 放入的数据
    :return: 加入元素到q中
    '''
    q.append(data)
#出队
def out(q):
    del q[0]
#感染周围的橘子,n代表了它旁边的橘子是第几次腐烂的
def change(grid,row,col,maxrow,maxcol,q,n):
    #进行标记,查看该位置的腐烂度
    if row==maxrow and col==maxcol:
        return
    if row+1<=maxrow and grid[row+1][col] == 1:
        #给应该腐烂的橘子进行标记,n+2代表了是第n次腐烂的橘子，而第n次腐烂的橘子
        #给予标识n+2，以便从队列取出时，就知道该位置的[值]-2就是腐烂的次数,依次循环
        #最终找到最后的n,输出就是结果
        grid[row+1][col] = 2+n
        comin(q,[row+1,col])
    if col + 1 <= maxcol and grid[row][col+1] == 1:
        grid[row][col+1] = 2+n
        comin(q,[row,col+1])
    if col - 1 >=0 and grid[row][col - 1] == 1:
        grid[row][col-1] = 2+n
        comin(q, [row, col-1])
    if row - 1 >= 0 and grid[row-1][col] == 1:
        grid[row-1][col] = 2+n
        comin(q,[row-1,col])
#遍历查找腐烂的橘子
def add2(grid,q):
    i = 0
    j = 0
    while (i <= maxrow):
        while (j <= maxcol):
            if grid[i][j] == 2:
                comin(q, [i, j])
            j += 1
        j = 0
        i += 1
    i = 0
#遍历查找新鲜橘子
def add1(grid,q):
    i = 0
    j = 0
    while (i <= maxrow):
        while (j <= maxcol):
            if grid[i][j] == 1:
                return True
            j += 1
        j = 0
        i += 1
    i = 0
grid = [[2,0,1],[1,1,1],[0,0,1]]
#q是一个队列，里面的元素是烂橘子的坐标[row,col]
q = []
maxrow = 3 - 1
maxcol = 3 - 1
num = 0
#第一轮遍历，找出所有腐烂的橘子，并且加入队列
add2(grid,q)
#若队列为空则输入-1表示没有烂橘子
if(len(q)==0):
    print(-1)
#定义数组v[row,col,n+2]其中n+2代表这是第几次变烂的橘子
#最后输出n即可
n = 0
while(len(q)!=0):
    #取出队列中的元素
    v = [q[0][0], q[0][1], grid[q[0][0]][q[0][1]]]
    #查看取出橘子是第几次烂的,那么它旁边的橘子就会是n+1的腐烂次数
    #grid在该位置的值-2就是它的腐烂次数，那么下次传入函数的腐烂次数应该+1
    n = v[2]-2
    row = v[0]
    col = v[1]
    del q[0]
    #所以在这里，将腐烂次数+1,传入n+1
    change(grid,row,col,maxrow,maxcol,q,n+1)
#如果还有新鲜橘子，说明不能完全腐烂
if add1(grid,q):
    print(-1)
else:
    print(n)
print(grid)