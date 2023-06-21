"""
接雨水
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
"""

def tomax(list):
    lens = len(list)
    m = list[0]
    i =0
    while(i+1<lens):
        if m<list[i+1]:
            m = list[i+1]
            i += 1
        else:
            i += 1
    return m

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
height = [4,2,0,3,100,5]
#寻找第一个非零点,并且-1
print(tomax(height))
temp = [4,2,0,3,100,5]
i= (len(temp)-2)//2
while(i>=0):
    make_heap(temp,i)
    i -= 1
#找出最高点,确定循环次数
#一层一层遍历
maxH = temp[0]
j = 0   #控件
ptr = 0 #指针
num = 0 #水量
q = 0
while(j<maxH):
    # 找0
    while height[ptr] == 0:
        ptr += 1
    while(ptr<len(height)):
        #找非0
        while ptr+1<len(height) and height[ptr+1]!=0:
            #此时指针指向了第一个空档位
            ptr += 1
        if ptr != len(height)-1:
            left = ptr
            ptr += 1
        #测距
        while ptr+1<len(height) and height[ptr+1]==0:
            ptr += 1
        if ptr != len(height)-1:
            right = ptr
            ptr += 1
            num = right - left + num
        if ptr == len(height)-1:
            break

    while(q<len(height)):
        if(height[q]!=0):
            height[q] = height[q] - 1
        q += 1
    q = 0
    ptr = 0
    j += 1
print(num)
