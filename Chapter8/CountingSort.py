#计数排序
#计算元素的个数放入C  用来反向排序
#
def countingsort(alist,k):
    l=len(alist)
    C = [0]*(k+1)
    B = [0]*l
    for i in range(0,len(alist)):
        C[alist[i]]=C[alist[i]]+1

    for i in range(0,k):
        C[i+1]=C[i]+C[i+1]

    for i in range(len(alist)-1,-1,-1):
        B[C[alist[i]]-1]=alist[i]
        C[alist[i]]=C[alist[i]]-1
        #print(B)
    return B

if __name__ == '__main__':
    alist = [2, 5, 3, 0, 2, 3, 0, 3]
    print("原列表为：%s" % alist)
    max=max(alist)
    out=countingsort(alist,max)
    print("新列表为：%s" % out)
    print(alist[0])