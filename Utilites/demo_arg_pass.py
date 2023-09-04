import argparse
import unittest



parser = argparse.ArgumentParser(description='Calculate values of two numbers')
parser.add_argument('-browser',default='chrome', type=str, help='string1')
parser.add_argument('-excu',default='local', type=str, help='string2')
args = parser.parse_args()

browser=args.browser
excu=args.excu
if __name__ == '__main__':
    from Tests.demo_test import MainTest
    test_suite = unittest.TestSuite()

    # Add test methods to the test suite
    # test_suite.addTest(unittest.makeSuite(MainTest))
    test_suite.addTest(MainTest('test_example_1'))
    test_suite.addTest(MainTest('test_example_2'))
    test_suite.addTest(MainTest('test_example_3'))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
