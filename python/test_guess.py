import unittest
import guess_2

class GuessTestCase(unittest.TestCase):


    #@classmethod
    #def setUpClass(cls):

    def setUp(self):

        print("请指定猜数字游戏的数字范围:")
        lowest = int(input("请输入数字范围的下限:\n"))
        highest = int(input("请输入数字范围的上限:\n"))
        print("游戏开始")
        guess_num = int(input("请输入你猜测的数字:\n"))

        guess = guess_2.game(lowest, highest)

        #获取待测的数据
        #num是要要取的猜的正确值
        self.real_num = guess.real_num
        # times是猜对所需的次数
        self.times = guess.times
        # msg是提示信息的实际值
        self.msg = guess.guess(guess_num)

    def test_guess(self, guess_num):

        #编写测试方法
        while guess_num == self.real_num:
            if self.times == 1:
                def test_guess_onetime_right(self):
                    #还没把list中的first_string取出来
                    self.assertEqual(self.msg[0], "You got it at the first time!!!")
                    #self.assertMultiLineEqual("{}".format(first_string), "You got it at the first time!!!")
            else:
                def test_guess_right(self):
                    #打算用string类型的包含方法来断言，但是没有找到这种方法
                    # 还没把list中的right_string取出来
                    self.assertEqual(self.msg[3], "You got it in {} times".format(self.times))

        if guess_num < self.real_num:
            def test_guess_low(self):
                # 还没把list中的low_string取出来
                self.assertEqual(self.msg[1], "Greater please")
        if guess_num > self.real_num:
            def test_guess_great(self):
                # 还没把list中的great_string取出来
                self.assertEqual(self.msg[2], "Lower please")


if __name__ == '__main__':



    #guessTest = GuessTestCase()
    #guessTest.test_guess(guess_num)

    #unittest.main()

    suite1 = unittest.TestLoader().loadTestsFromTestCase(GuessTestCase)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)



