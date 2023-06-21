"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成两笔交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1:
输入：prices = [3,3,5,0,0,3,1,4]
输出：6
输入：prices = [1,2,3,4,5]
输出：4
示例 3：
输入：prices = [7,6,4,3,1]
输出：0
示例 4：
输入：prices = [1]
输出：0
"""

"""
很简单，找出所有能赚钱的买卖法，每次赚钱存在数组p[]中,p[n]表示第n次赚到的钱
只许将p[]遍历两次找出两个最大值即可,这是贪心算法，不保证找到最终的最优解
下面是代码实现:
"""
prices = [1,2,4,2,5,7,2,4,9,0]
#表示天数
alldays = len(prices)-1
#have表示是否持有股票
have = False
day = 0
p = []
while(day<=alldays):
    money = 0
    #找出极小值点,买入股票
    while(day+1<=alldays and prices[day]>=prices[day+1]):
        day += 1
    #先判断：如果是最后一天了，没必要买入了，就结束了
    if day == alldays:
        break
    if have == False :
        money -= prices[day]
        have = True
    while(day+1<=alldays and prices[day]<=prices[day+1]):
        day += 1
    #先判断，如果是最后一天了，就没必要等了，直接卖出
    if day == alldays and have == True:
        money += prices[day]
        p.append(money)
        break
    if have == True :
        money += prices[day]
        #赚的钱计入记录
        p.append(money)
        have = False
#如果根本没赚钱，就输出0
print(p)
if(len(p)==0):
    print(0)

#遍历两次p,找出最大的两个值,相加输出即可
#这里使用建立堆的方式快速找出两个最大值,建立大根堆
def make_heap(p,root):
    #先判断有没有左孩子
    if(2*root+1>=len(p)):
        return
    #再判断有没有右孩子
    if 2*root+2>=len(p):
        if p[root]<p[2*root+1]:
            p[root],p[2*root+1] = p[2*root+1],p[root]
        return
    #若都有，则选择出三者最大
    son = 2*root+1
    if p[2*root+1]<p[2*root+2] :
        son = 2*root+2
    if p[son]>p[root]:
        p[son],p[root] = p[root],p[son]
    #向下递归，维护底层的根堆性质
    make_heap(p,2*root+1)
    make_heap(p,2*root+2)
#如果就赚了一次钱，就直接输出
if(len(p)==1):
    print(p[0])
else:
    #从第一个非子叶节点开始建堆
    i= (len(p)-2)//2
    while(i>=0):
        make_heap(p,i)
        i -= 1
    #取出堆顶元素并删除
    one = p[0]
    del p[0]
    #再建一次堆
    i = (len(p)-2)//2
    while(i>=0):
        make_heap(p,i)
        i -= 1
    two = p[0]
    answer = one + two
    print(answer)


    