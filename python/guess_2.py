#因进行单元测试，重构猜数字游戏的方法
import  random

class game():
    def __init__(self, lowest, highest):
        self.lowest = lowest
        self.highest = highest
        self.real_num = random.randint(self.lowest, self.highest)
        self.first_string = 'You got it at the first time!!!'

        self.low_string = 'Greater please'
        self.great_string = 'Lower please'

    """
    def __get__num(self):
        self.real_num = random.randint(self.lowest, self.highest)
        return self.real_num
    """

    def guess(self, guess_num):


        times = 1
        msg = []

        if guess_num == self.real_num:
            #print("{}".format(self.first_string))
            print(self.first_string)
            #msg.append(self.first_string)
            msg[0] = self.first_string

        while guess_num != self.real_num:

            times = times + 1

            if guess_num < self.real_num:
                print(self.low_string)
                #msg.append(self.low_string)
                msg[1] = self.low_string
            else:
                print(self.great_string)
                #msg.append(self.great_string)
                msg[2] = self.great_string

            guess_num = int(input())

        if times != 1:
            right_string = "You got it in {} times".format(times)
            print(right_string)
            #msg.append(right_string)
            msg[3] = self.right_string

        return msg

if __name__ == '__main__':
    print("请指定猜数字游戏的数字范围:")
    lowest = int(input("请输入数字范围的下限:\n"))
    highest = int(input("请输入数字范围的上限:\n"))

    guessNum = game(lowest, highest)

    print("游戏开始")
    guess_num = int(input("请输入你猜测的数字:\n"))

    msg = guessNum.guess(guess_num)

    #print(msg[0])



