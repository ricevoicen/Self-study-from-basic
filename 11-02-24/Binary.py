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
