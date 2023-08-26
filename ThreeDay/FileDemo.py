import os

f = open("D:\Temp\hello.txt", "rt", encoding='utf-8')
print(f.read())
f.close()

print("------------------")

# 只读取文件的一部分
f = open("D:\Temp\hello.txt", "rt", encoding='utf-8')
print(f.read(3))
f.close()

print("------------------")

# 读取一行
f = open("D:\Temp\hello.txt", "rt", encoding='utf-8')
print(f.readline())
f.close()

print("------------------")

# 循环遍历
f = open("D:\Temp\hello.txt", "rt", encoding='utf-8')
for x in f:
    print(x)

f.close()

print("------------------")

# 追加写入文件
f = open("D:\Temp\hello.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("D:\Temp\hello.txt", "r", encoding='utf-8')
print(f.read())
f.close()

print("------------------")

# 覆盖写入文件
f = open("D:\Temp\hello.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("D:\Temp\hello.txt", "r", encoding='utf-8')
print(f.read())
f.close()

print("------------------")

# 创建新文件
f = open("D:\Temp\myFile.txt", "w")
f.close()

print("------------------")

# 删除文件
if os.path.exists("D:\Temp\myFile.txt"):
    os.remove("D:\Temp\myFile.txt")
else:
    print("The file does not exist")

print("------------------")

# 删除文件夹
os.rmdir("D:\Temp\myFolder")  # 提示：您只能删除空文件夹。
