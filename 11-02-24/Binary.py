# 提示用户输入第一个数字n，然后循环n次，每次提示用户输入一个数字
# n > 0
n = int(input("请输入一个正整数n: "))
while n <= 0:
    n = int(input("输入无效，请输入一个正整数n: "))

# Create an empty list to store numbers
mindo = []
for i in range(n):
    num = float(input(f"请输入第{i+1}个数字: "))
    mindo.append(num)  # Add each number to the list

# Determine which sorting algorithm to use based on array length
n_length = len(mindo)

if n_length < 50:
    # Insertion Sort for small arrays
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    sorted_array = insertion_sort(mindo)

elif n_length < 1000:
    # Quick Sort for medium arrays
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
    sorted_array = quick_sort(mindo)

else:
    # Merge Sort for large arrays
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        return merge(left, right)
    
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    sorted_array = merge_sort(mindo)

print("排序后的数组:", sorted_array)

