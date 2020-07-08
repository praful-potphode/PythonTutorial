# 'unittest' supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections,
# and independence of the tests from the reporting framework.
#
# The unittest module provides classes that make it easy to support these qualities for a set of tests.
#
# To achieve this, unittest supports the following important concepts −
#
# test fixture − This represents the preparation needed to perform one or more tests, and any associate cleanup actions.
# This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.
#
# test case − This is the smallest unit of testing. This checks for a specific response to a particular set of inputs.
# unittest provides a base class, TestCase, which may be used to create new test cases.
#
# test suite − This is a collection of test cases, test suites, or both. This is used to aggregate tests that should be
# executed together. Test suites are implemented by the TestSuite class.
#
# test runner − This is a component which orchestrates the execution of tests and provides the outcome to the user.
# The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of
# executing the tests.
# Creating a Unit Test
# The following steps are involved in writing a simple unit test −
#
# Step 1 − Import the unittest module in your program.
#
# Step 2 − Define a function to be tested. In the following example, add() function is to be subjected to test.
#
# Step 3 − Create a testcase by subclassing unittest.TestCase.
#
# Step 4 − Define a test as a method inside the class. Name of method must start with 'test'.
#
# Step 5 − Each test calls assert function of TestCase class. There are many types of asserts. Following example calls assertEquals() function.
#
# Step 6 − assertEquals() function compares result of add() function with arg2 argument and throws assertionError if comparison fails.
#
# Step 7 − Finally, call main() method from the unittest module.
import unittest


def add(x, y):
    return x + y


class SimpleTest(unittest.TestCase):
    def testadd1(self):
        self.assertEquals(add(4, 5), 9)


if __name__ == '__main__':
    unittest.main()