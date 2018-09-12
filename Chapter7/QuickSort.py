#快速排序
#迭代方法
def quicksort(alist,p,r):
    if p<r:
        print(alist)
        q=partition(alist,p,r)
        quicksort(alist,p,q-1)
        quicksort(alist,q+1,r)


def partition(alist,p,r):
    x=alist[r]
    i=p-1
    for j in range(p,r):
        if alist[j]<=x:
            i=i+1
            so=alist[j]
            alist[j]=alist[i]
            alist[i]=so

    so=alist[r]
    #print(j)
    alist[r]=alist[i+1]
    alist[i+1]=so
    #print(alist)
    return i+1


if __name__ == '__main__':
    alist = [2, 8, 7, 1, 3, 5, 6, 4]
    print("原列表为：%s" % alist)
    quicksort(alist,0,len(alist)-1)
    print("新列表为：%s" % alist)
