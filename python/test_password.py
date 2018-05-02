import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('set up')
        self.test_data = [
            dict(name = 'jack', password = 'woaiwojia'),
            dict(name = 'rose', password = 'ilovejack'),
            dict(name = 'tom', password = 'password123')
        ]
    def test_week_password(self):
        for data in self.test_data:
            password = data['password']
            name = data['name']
            self.assertTrue(len(password) >= 6)

            msg = "{}的密码是弱密码".format(name)
            self.assertTrue(password != 'password', msg)
            self.assertTrue(password != 'password123', msg)


if __name__ == '__main__':
    unittest.main()
