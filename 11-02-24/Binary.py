# Add these at the very beginning of your file
import os
os.environ["PYTHONUTF8"] = "1"  # Enable UTF-8 mode on Windows
os.environ["PYTHONIOENCODING"] = "utf-8"

# Add encoding specification
# -*- coding: utf-8 -*-

# 提示用户输入一个正整数n作为数组长度
n = int(input("请输入一个正整数n: "))
while n <= 0:
    n = int(input("输入无效，请输入一个正整数n: "))

# 创建一个包含n个随机数的数组
import random
mindo = [random.randint(1, 100) for _ in range(n)]
print(f"原始数组: {mindo}")

# 根据数组长度选择排序算法
n_length = len(mindo)

if n_length < 50:
    # 插入排序，显示每一步
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            print(f"\n第{i}轮插入排序:")
            print(f"当前要插入的元素: {key}")
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            print(f"本轮排序后: {arr}")
        return arr
    
    print("\n使用插入排序算法:")
    sorted_array = insertion_sort(mindo)

elif n_length < 1000:
    # 快速排序，显示每一步
    def quick_sort(arr, start=0, end=None):
        if end is None:
            end = len(arr) - 1
        
        if start < end:
            print(f"\n当前处理的子数组: {arr[start:end+1]}")
            pivot = arr[end]
            print(f"选择的基准值: {pivot}")
            i = start - 1
            
            for j in range(start, end):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[end] = arr[end], arr[i + 1]
            print(f"分区后的数组: {arr}")
            
            quick_sort(arr, start, i)
            quick_sort(arr, i + 2, end)
        return arr
    
    print("\n使用快速排序算法:")
    sorted_array = quick_sort(mindo.copy())

else:
    # 归并排序，显示每一步
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        print(f"\n分割数组: {arr}")
        print(f"左半部分: {arr[:mid]}")
        print(f"右半部分: {arr[mid:]}")
        
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        return merge(left, right)
    
    def merge(left, right):
        result = []
        i = j = 0
        print(f"\n合并: {left} 和 {right}")
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        print(f"合并后: {result}")
        return result
    
    print("\n使用归并排序算法:")
    sorted_array = merge_sort(mindo.copy())

print(f"\n最终排序结果: {sorted_array}")

