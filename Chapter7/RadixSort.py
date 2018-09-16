#基数排序
#调用冒泡排序对一位数排序
def bubbleSort(seq,c):  #seq是位数的序列 即求模结果，C是原始数列
    for i in range(len(seq)):
        for j in range(len(seq) - 1, i, -1):
            if seq[j] < seq[j - 1]:
                seq[j - 1], seq[j] = seq[j], seq[j - 1]
                c[j-1],c[j]=c[j],c[j-1]

def radixsort(alist,d):
    mod=[0]*len(alist)
    for i in range(0,d):
        for j in range(len(alist)):
            mod[j]=(alist[j]//10**(i))%10   #按照从低位到高位排序
        bubbleSort(mod, alist)
       #for i in range(len(alist)):
        #   mod[i]=po[i]%10    #模
        #   po[i] = po[i] // 10  # 余

if __name__ == '__main__':
    alist = [329, 457, 657, 839, 436, 720, 355]
    print("原列表为：%s" % alist)
    radixsort(alist,3)  #输入序列和数字位数
    print("新列表为：%s" % alist)