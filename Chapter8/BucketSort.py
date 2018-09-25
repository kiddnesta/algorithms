import math
#桶内排序
def insert_sort(alist):  #升序排序 插入排序
    len1=len(alist)
    for i in range(1,len1):
        key=alist[i]   #对第j的元素插序，前j-1个已经排序好了 key是需要排序的新数
        j=i-1
        while j>=0 and alist[j]>key:  #排序条件 对第j个比较，如果小于key的就结束
            alist[j+1]=alist[j]  #把j个数放入j+1
            j=j-1       #再比较前一个
        alist[j+1]=key  #结束的话 key放入j+1


def BucketSort(alist):
    n=len(alist)
    b = [[] for i in range(10)]   #初始化二维桶
    for i in range(0,n):
        b[math.floor(alist[i]*10)].append(alist[i])
    for i in range(0,n):
        insert_sort(b[i])
    #b是已经排序好的桶
    result=[]
    for i in range(0,n):
        result.extend(b[i])
    result=[result[i]*20 for i in range(0,n)] #list计算很特殊
    print(result)


if __name__ == '__main__':
    AA = [9, 15, 17, 10, 16, 3, 14, 12, 1, 4]
    BB = [i / 20.0 for i in AA]
    print(BB)
    BucketSort(BB)
    print(BB)
