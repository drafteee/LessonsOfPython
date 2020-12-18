import unittest
import functions


class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        test_param = 10
        result = functions.do_stuff(test_param)
        self.assertEqual(result, 10)

    def test_do_stuff_value(self):
        test_param2 = '1fsdf'
        result2 = functions.do_stuff(test_param2)
        self.assertEqual(result2, ValueError)

    def test_do_stuff_instance(self):
        test_param2 = '1fsdf'
        result2 = functions.do_stuff(test_param2)
        self.assertIsInstance(result2, ValueError)

    def test_do_stuff_instance2(self):
        test_param2 = None
        result2 = functions.do_stuff(test_param2)
        self.assertEqual(result2, "dssadsa")

    def tearDown(self):
        print('clean')


if __name__ == '__main__':
    unittest.main()
