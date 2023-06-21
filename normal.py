
print('hello world')
list = [1,2,3,'me','i']
print(list[3])
'''
多行注释
多行注释
'''
def max(a,b):
    if(a>b):
        return a
    else:
        return b
def maxs(list,n):
    '''
    :param list:那一条银行街道
    :param n: 代表多少家银行
    :return: 返回前偷前N家银行的最大金额
    '''
    if(n==0):
        return 0
    if(n==1):
        return list[1]
    if(n==2):
        return max(list[1],list[2])
    if(n>2):
        return max(list[n]+maxs(list,n-2),maxs(list,n-1))
"""
maxs(list,n) = 值           代表偷了前n家得到的最多的钱
"""
list =[0,0,0,0,0,0,0,0,0,0,0,0,0,2,6]
n = list.__len__()
print(maxs(list,n-1))
# pargam = {"ok":10,"fjr":"lyh"}
# print(pargam["fjr"])
"""
bfs例子:
Leetcode 994.腐烂的橘子
"""
#输入:
grid = [[2,1,1],[1,1,0],[0,1,1]]
queue = []
base = 0
last = 0
queue.append([1,1])
queue.append([1,1])
queue.append([1,1])