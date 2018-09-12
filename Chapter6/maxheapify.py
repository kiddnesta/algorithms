#保持最大堆特性
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
    alist = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    print("原列表为：%s" % alist)
    maxheapify(alist,1)
    print("新列表为：%s" % alist)
