"""
恶魔们抓住了公主并将她关在了地下城dungeon 的 右下角 。地下城是由 m x n 个房间组成的二维网格。我们英勇的骑士最初被安置在 左上角 的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。

为了尽快解救公主，骑士决定每次只 向右 或 向下 移动一步。

返回确保骑士能够拯救到公主所需的最低初始健康点数。

注意：任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。

示例 1：
输入：dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
输出：7
解释：如果骑士遵循最佳路径：右 -> 右 -> 下 -> 下 ，则骑士的初始健康点数至少为 7 。
示例 2：
输入：dungeon = [[0]]
输出：1
"""
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
#记忆化搜索加剪枝优化
stack = []
#入栈(并且更新栈顶)
top = -1
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


#dp动态规划求解 dp[i][j]表示在[i,j]这个点需要的最少健康值
"""
递推式:dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + dungeon[i][j]
"""
dp = [[0,0,0],[0,0,0],[0,0,0]]
dp[0][0]=dungeon[0][0]
i =0
j =0
while(i<len(dungeon)):
    while(j<len(dungeon)):
        if i==0 and j==0:
            dp[i][j] = dungeon[0][0]
            j +=1
        elif i==0:
            if dungeon[i][j]>0:
                dp[i][j] = dp[i][j-1]
                j += 1
            else:
                dp[i][j] = dp[i][j-1]+dungeon[i][j]
                j += 1
        elif j==0:
            if dungeon[i][j]>0:
                dp[i][j] = dp[i-1][j]
                j += 1
            else:
                dp[i][j] = dp[i-1][j]+dungeon[i][j]
                j += 1
        else:
            if dungeon[i][j]>0:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                j += 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])+dungeon[i][j]
                j += 1
    j = 0
    i += 1
print(dp[2][2])