#构建最大堆
#用保持最大堆的方法 从n/2--1
import math
def buildmaxheap(alist):
    l=math.floor(len(alist)/2)-1
    for i in range(l,-1,-1):
        maxheapify(alist,i)
        #print(alist)


def maxheapify(alist,i):
    left=2*i+1   #左子节点 右子节点
    right=2*i+2
    l=len(alist)-1
    if left<=l and alist[left]>alist[i]: #防止堆超过长度
        max=left
    else:
        max=i
    if right<=l and alist[right]>alist[max]: #防止堆超过长度
        max=right
    else:
        pass
    if max!=i:
        ex=alist[i]
        alist[i]=alist[max]
        alist[max]=ex
        maxheapify(alist,max)
    pass


if __name__ == '__main__':
    alist = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print("原列表为：%s" % alist)
    buildmaxheap(alist)
    print("新列表为：%s" % alist)
