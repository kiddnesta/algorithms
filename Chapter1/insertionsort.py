#插入排序程序
def insert_sort(alist):  #升序排序 插入排序
    len1=len(alist)
    for i in range(1,len1):
        key=alist[i]   #对第j的元素插序，前j-1个已经排序好了 key是需要排序的新数
        j=i-1
        while j>=0 and alist[j]>key:  #排序条件 对第j个比较，如果小于key的就结束
            alist[j+1]=alist[j]  #把j个数放入j+1
            j=j-1       #再比较前一个
        alist[j+1]=key  #结束的话 key放入j+1


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("原列表为：%s" % alist)
    insert_sort(alist)
    print("新列表为：%s" % alist)
    print(alist[0])
# 结果如下：
# 原列表为：[54, 26, 93, 17, 77, 31, 44, 55, 20]
# 新列表为：[17, 20, 26, 31, 44, 54, 55, 77, 93]