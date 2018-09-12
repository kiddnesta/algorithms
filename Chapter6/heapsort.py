#堆排序算法
#用建立最大堆的算法 A[1]是最大值
#取出A[1]，剩下的继续维持最大堆，提取最大值。
import math
def heapsort(alist):
    buildmaxheap(alist)
    seq=[]
    for i in range(0,len(alist)):
        seq.append(alist[0])
        alist.pop(0)
        maxheapify(alist,0)
    seq.reverse()
    return seq
    pass


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
    seq=heapsort(alist)
    print("新列表为：%s" % seq)
