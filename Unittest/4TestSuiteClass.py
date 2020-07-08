# TestSuite Class
# Python's testing framework provides a useful mechanism by which test case instances can be grouped together according '\
# 'to the features they test. This mechanism is made available by TestSuite class in unittest module.
#
# The following steps are involved in creating and running a test suite.
# Step 1 − Create an instance of TestSuite class.
# suite = unittest.TestSuite()
#
# Step 2 − Add tests inside a TestCase class in the suite.
# suite.addTest(testcase class)
#
# Step 3 − You can also use makeSuite() method to add tests from a class
# suite = unittest.makeSuite(test case class)
#
# Step 4 − Individual tests can also be added in the suite.
# suite.addTest(testcaseclass(""testmethod")
#
# Step 5 − Create an object of the TestTestRunner class.
# runner = unittest.TextTestRunner()
#
# Step 6 − Call the run() method to run all the tests in the suite
# runner.run (suite)

# 1	addTest()
# Adds a test method in the test suite.
#
# 2	addTests()
# Adds tests from multiple TestCase classes.
#
# 3	run()
# Runs the tests associated with this suite, collecting the result into the test result object
#
# 4	debug()
# Runs the tests associated with this suite without collecting the result.
#
# 5	countTestCases()
# Returns the number of tests represented by this test object

import unittest
# from .2TestcaseClass import  TestcaseClass

class suiteTest(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 20

    def testadd(self):
        """Add"""
        result = self.a + self.b
        self.assertTrue(result == 100)

    def testsub(self):
        """sub"""
        result = self.a - self.b
        self.assertTrue(result == -10)


def suite():
    suite = unittest.TestSuite()
    ##   suite.addTest (simpleTest3("testadd"))
    ##   suite.addTest (simpleTest3("testsub"))
    suite.addTest(unittest.makeSuite(TestcaseClass))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
    # You     can    experiment with the addTest() method by uncommenting the lines
    # and comment statement having makeSuite() method.