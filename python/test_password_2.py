import unittest
import json

class PasswordWithJsonTestCase(unittest.TestCase):
    @ classmethod
    #def setUpClass(self):
    def setUpClass(cls):
        print('在所有测试方法前都重读一次测试数据')
        data_file_path = './user_data.json'
        with open(data_file_path) as f:
            cls.test_data = json.loads(f.read())

    def test_week_password(self):
        res = True
        msg = []
        for data in self.test_data:
            password = data['password']
            name = data['name']
            temp_res = True

            temp_res = temp_res and len(password) >= 6
            temp_res = temp_res and password != "password"
            temp_res = temp_res and password != "password123"

            if not temp_res:
                msg.append("{}的密码太弱了".format(name))
            res = res and temp_res
        self.assertTrue(res, "\n".join(msg))

if __name__ == '__main__':
    unittest.main()
