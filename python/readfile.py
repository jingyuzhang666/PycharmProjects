#用自己的方法跳过命令行 and 读文件

path = "C:\\Users\\intasect\\PycharmProjects\\python\cs.txt"
file_obj = open(path)
print(file_obj.read())
file_obj.close()