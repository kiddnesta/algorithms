#分治排序程序的迭代算法
#一个序列不停地二分，最后得到单独的一个数的序列
#然后用分支排序重新组合
import math
def mergesort(A,start,end):
    if start<end:
        mid=math.floor((start+end)/2)
        mergesort(A,start,mid)
        mergesort(A,mid+1,end)
        merge(A,start,mid,end)


def merge(A,start,mid,end):  # 升序排序 插入排序
    i=start
    j=mid+1
    seq=[]
    print(start, mid, end)
    while i<=mid and j<=end:
        #print(i,j,start,mid,end)
        if A[i]<A[j]:
            seq.append(A[i])
            i=i+1
        else:
            seq.append(A[j])
            j=j+1
    if i>mid:
        seq.extend(A[j:end+1])
    else:
        seq.extend(A[i:mid+1])
    A[start:end+1]=seq[:]
    #print(A)

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 34, 71, 90,23,41,345,12]
    mergesort(alist,0,len(alist)-1)
    print(alist)