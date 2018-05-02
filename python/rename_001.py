# 获取命令行参数失败，原因：又不是cmd，怎么传命令过去
from sys import argv

script, case_id = argv
print(f"输入对话编号", {case_id})
name = input("请输入姓名：\n")
age = input("请输入年龄\n")
sex = input("请输入性别\n")

formatter = """
对话编号：{}
姓名：{}
年龄：{}
性别：{}
"""

print(formatter.format(case_id, name, age, sex))