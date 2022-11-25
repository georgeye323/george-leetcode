import time
import random


def bubble_sort(lst: list)-> list:
    """
    1.冒泡排序(bubble sort)
        比较两个相邻的元素。如果第一个比第二个大，就交换他们两个。
        对每一组相邻元素做同样的工作，从开始到第一对到结尾的最后一对，这样在最后的元素应该是最大的数
        针对所有的元素重复以上的步骤，除了最后一个
    时间复杂度：
        每轮操作n次，总共有n轮，时间复杂度为O(n^2)
    空间复杂度：
        额外空间的开销在交换数据时那一个过渡空间，空间复杂度为O(1)
    """
    # 1、计算列表的大小
    # print(f"排序前的列表{lst}")
    list_length = len(lst)
    if list_length <= 1:
        # 如果列表长度小于或等于1，直接返回
        return  list
    # 2、外层循环
    for i in range(list_length):
        for j in range(0,list_length-i-1):
            # 如果前一个数大于后一个数，需要交换位置
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
    # print(f"排序后的列表 {lst}")
    return lst


def quick_sort(lst: list)->list:
    """
    2、快速排序(quick sort)
        从列表中挑出一个元素，作为“基准”
        重新排序列表，所有比基准小的放在基准前面，所有比基准大的放在后面
        递归的把小于基准元素的子列表和大于基准的子列表进行排序
    时间复杂度：
       基准值若能把数据分为平均的两块，划分次数O(logn)，每次划分遍历比较一遍O(n)，时间复杂度O(nlogn)。
    空间复杂度：
        额外空间开销出在暂存基准值，O(logn)次划分需要O(logn)个，空间复杂度O(logn)
    """

    def partition(lst, left, right):
        """进行分区操作"""
        key = left
        while left < right:
            while left < right and lst[right] >= lst[key]:
                right -= 1
            while left < right and lst[left] <= lst[key]:
                left += 1
            lst[left], lst[right] = lst[right], lst[left]
        lst[left], lst[key] = lst[key], lst[left]
        return  left

    def quicksort(lst, left, right):
        if left >= right:
            return
        mid = partition(lst, left, right)
        quicksort(lst, left, mid-1)
        quicksort(lst, mid+1, right)

    n = len(lst)
    if n <= 1:
        return lst
    quicksort(lst, 0, n-1)
    return lst



def insert_sort(lst: list)->list:
    """
    3、插入排序(insert sort)
        从第一个元素开始，该元素可以认为已经被排序
        取下一个元素，在已经排序的元素序列中从后向前扫描
        如果该元素大于新元素，将该元素移动到下一位置
     时间复杂度：
        每轮操作n次，总共有n轮，时间复杂度为O(n^2)
    空间复杂度：
        额外空间的开销在数据移动位置时那一个过渡空间，空间复杂度为O(1)
    :return:list
    """
    list_length = len(lst)
    if list_length <= 1:
        return lst
    for i in range(1, list_length):
        for j in range(i):
            if lst[i] < lst[j]:
                lst.insert(j, lst[i])
                lst.pop(i+1)
                break
    return lst


def select_sort(lst: list)->list:
    """
    4、选择排序(select sort)
        首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
        然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
        以此类推，直到所有元素均排序完毕
    :param lst:
    :return:
    """
    n = len(lst)
    if n <= 1:
        return  lst
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if lst[min_index] > lst[j]:
                min_index = j
            lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


def shell_sort(lst: list)->list:
    """
    5、希尔排序(shell sort)
        。希尔排序也是一种插入排序，它是简单插入排序经过改进之后的一个更高效的版本，也称为缩小增量排序，
        同时该算法是冲破O(n2）的第一批算法之一。
        它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。
    :param lst:
    :return: list
    """
    n = len(lst)
    if n <= 1:
        return lst
    gap = n // 2
    while gap:
        for i in range(gap, n):
            while i - gap >= 0 and lst[i-gap] > lst[i]:
                lst[i-gap], lst[i] = lst[i], lst[i-gap]
                i -= gap
        gap //= 2
    return lst

def merge_sort(lst: list)->list:
    """
    6、归并排序(merge sort)
         是建立在归并操作上的一种有效的排序算法。
         该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
         归并排序是一种稳定的排序方法。将已有序的子序列合并，得到完全有序的序列；
         即先使每个子序列有序，再使子序列段间有序。
         若将两个有序表合并成一个有序表，称为2-路归并。
    :param lst:
    :return:
    """
    if len(lst) <= 1:
        return lst
    min_index = len(lst) // 2
    left = merge_sort(lst[:min_index])
    right = merge_sort(lst[min_index:])
    return merge(left, right)

def merge(left, right):
    result = list()
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return  result



if __name__ == "__main__":
    """生成长度为10000的乱序列表"""
    li =[_ for _ in range(10000)]
    random.shuffle(li)
    start_time = time.time()
    print(f"start_time is {start_time}")
    shell_sort(li)
    end_time = time.time()
    print(f"花费时间为 {end_time - start_time}")

