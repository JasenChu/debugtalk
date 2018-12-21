# 实现2路归并排序算法

def merge(leftSource = [], rightSource = []):
    lenLeft = len(leftSource)
    lenRight = len(rightSource)
    # 定义存储合并后的list数组
    merge_one = [0] * (lenLeft + lenRight)
    mi = 0 # 定义合并list的下标
    li = 0 # 定义左边数组的下标
    ri = 0 # 定义右边数组的下标
    while li < lenLeft and ri < lenRight:
        # 左右和右边依次取第一个数字比较，小的放合并数组中
        if leftSource[li] <= rightSource[ri]:
           merge_one[mi] = leftSource[li]
           li = li + 1
        else:
            merge_one[mi] = rightSource[ri]
            ri = ri + 1
        mi = mi + 1
    if  li < lenLeft: # 判断左边数组是否已经取值完毕
        for i in range(li, lenLeft):
            merge_one[mi] = leftSource[i]
            mi = mi + 1
    else: # 判断右边数组是否已经取值完毕
        for j in range(ri, lenRight):
            merge_one[mi] = rightSource[j]
            mi = mi + 1 
    return merge_one

def merge_sort(to_sort = []):
    if len(to_sort) == 1:
        return to_sort
    mid = len(to_sort) // 2
    left = to_sort[:mid]
    right = to_sort[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    merged = merge(left, right)

    return merged

if __name__ == '__main__':
    print(merge_sort([10,20,9,50,30,99,3]))

    