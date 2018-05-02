# -*- coding: utf-8 -*-
import unittest


class MyTestCase(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('food'.upper(), 'FOOD')
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
"""
suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
"""