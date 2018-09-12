#分治排序程序
#先用插入排序对两个序列排序 然后合并
def insert_sort(alist):  # 升序排序 插入排序
    len1 = len(alist)
    for i in range(1, len1):
        key = alist[i]  # 对第j的元素插序，前j-1个已经排序好了 key是需要排序的新数
        j = i - 1
        while j >= 0 and alist[j] > key:  # 排序条件 对第j个比较，如果小于key的就结束
            alist[j + 1] = alist[j]  # 把j个数放入j+1
            j = j - 1  # 再比较前一个
        alist[j + 1] = key  # 结束的话 key放入j+1

def merge(alist,p,q,r):  # 升序排序 插入排序
    L=alist[p:q+1]
    R=alist[q+1:r+1]
    Llen=len(L)
    Rlen=len(R)
    i=0
    j=0
    alistnew=[0]*(r+1)
    for k in range(0,r):  #比较两个序列的取值  小的放入alistnew中
        if L[i]>R[j]:
            alistnew[k]=R[j]
            j = j + 1
            if j>Rlen-1:  #如果超过一个序列长度 直接把另一个剩余序列复制进去  代替哨兵
                alistnew[k+1:]=L[i+1:]
                break
        else:
            alistnew[k]=L[i]
            i = i + 1
            if i>Llen-1:  #如果超过一个序列长度 直接把另一个剩余序列复制进去  代替哨兵
                alistnew[k+1:]=R[j+1:]
                break
    #print(alistnew)
    return alistnew
    #print(L)
    #print(R)

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 34, 71]
    mid=int(len(alist)/2)
    alist1=alist[0:mid]
    alist2=alist[mid:]
    insert_sort(alist1)
    insert_sort(alist2)
    print("列表1排序为：%s" % alist1)
    print("列表2排序为：%s" % alist2)
    alist=alist1+alist2
    p=0
    q=mid-1
    r=len(alist)-1
    print(alist)
    print(p,q,r)
    alistnew=merge(alist,p,q,r)
    print(alistnew)
# 结果如下：
# 原列表为：[54, 26, 93, 17, 77, 31, 44, 55, 20]
# 新列表为：[17, 20, 26, 31, 44, 54, 55, 77, 93]