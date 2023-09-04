import unittest
from Utilites.demo_arg_pass import browser,excu
class MainTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.browser=browser
        cls.excu=excu
        if excu=='Local':
            if browser=='chrome':
                print("chrome browser")
            elif browser=='firefox':
                print('firefox browser')
            else:
                print('select correct browser')
        elif excu=='Grid':
            if browser=='chrome':
                print("chrome browser")
            elif browser=='firefox':
                print('firefox browser')
            else:
                print('select correct browser')
        else:
            print('wrong Choice')

    @classmethod
    def test_example_1(cls):
        # Your test implementation for test_example_1
        print(f'1st Test')
    @classmethod
    def test_example_2(cls):

        # Your test implementation for test_example_2
        print(f'2nd Test')
    @classmethod
    def test_example_3(cls):

        # Your test implementation for test_example_3
        print(f'3rd Test')

    @classmethod
    def tearDownClass(cls) -> None:
        print('All test finished...')


