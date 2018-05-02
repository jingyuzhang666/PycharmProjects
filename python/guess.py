# 猜数字
# 以后注意不要if套if，合适的运用if或while
import random
# import math

num = random.randint(1, 10)
#优化为for循环
for i in range(1, 10):
    guess = int(input('请输入1-10的数字:\n'))
    if guess != num:
      #for循环中的i本身就是自加的
        #i = i + 1
        if guess > num:
          print("Lower please")
        else:
          print("Greater please")
    else:
        if i == 1:
            print("You got it at the first time!!!")
        else:
            #注意python自带的format方法
            print("You got it in {} times".format(i))





