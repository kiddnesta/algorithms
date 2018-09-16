#冒泡排序
#比较相邻的 大的滞后
#历遍一轮 最后一个为最大值
#排序n-1
def bubblesort(alist):
    n=len(alist)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if alist[j]>alist[j+1]:
                key=alist[j+1]
                alist[j+1]=alist[j]
                alist[j]=key

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("原列表为：%s" % alist)
    bubblesort(alist)
    print("新列表为：%s" % alist)
