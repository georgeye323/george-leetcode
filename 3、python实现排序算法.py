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
        额外空间的开销在交换数据时那一个过滤空间，空间复杂度为O(1)
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



if __name__ == "__main__":
    """生成长度为10000的乱序列表"""
    li =[_ for _ in range(10000)]
    random.shuffle(li)
    start_time = time.time()
    print(f"start_time is {start_time}")
    bubble_sort(li)
    end_time = time.time()
    print(f"花费时间为 {end_time - start_time}")

