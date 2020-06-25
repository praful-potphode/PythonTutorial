# TestCase Class
# Object of this class represents the smallest testable unit. It holds the test routines and provides hooks for preparing
# each routine and for cleaning up thereafter.
# The following methods are defined in the TestCase class −
# 1.setUp()
# Method called to prepare the test fixture. This is called immediately before calling the test method
#
# 2.tearDown()
# Method called immediately after the test method has been called and the result recorded. This is called even if the test method raised an exception,
#
# 3.setUpClass()
# A class method called before tests in an individual class run.
#
# 4.tearDownClass()
# A class method called after tests in an individual class have run.
#
# 5.run(result=None)
# Run the test, collecting the result into the test result object passed as result.
#
# 6.skipTest(reason)
# Calling this during a test method or setUp() skips the current test.
#
# 7.debug()
# Run the test without collecting the result.

# 8. shortDescription()
# Returns a one-line description of the test.

# Fixtures
# There can be numerous tests written inside a TestCase class. These test methods may need database connection, temporary
# files or other resources to be initialized. These are called fixtures. TestCase includes a special hook to configure and
# clean up any fixtures needed by your tests. To configure the fixtures, override setUp(). To clean up, override tearDown().
# In the following example, two tests are written inside the TestCase class. They test result of addition and subtraction
# of two values. The setup() method initializes the arguments based on shortDescription() of each test. teardown() method
# will be executed at the end of each test.
import unittest
class TestcaseClass(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 20
        name = self.shortDescription()
        print('name',name)
        if name == "Add":
            self.a = 10
            self.b = 20
            print( name, self.a, self.b)
        if name == "sub":
            self.a = 50
            self.b = 60
            print( name, self.a, self.b)
        if name == "mul":
            self.a = 73
            self.b = 0.339
            print( name, self.a, self.b)
        if name == "div":
            self.a = 16
            self.b = 3
            print( name, self.a, self.b)

    def tearDown(self):
        print('\nend of test', self.shortDescription())

    def testadd(self):
        """Add"""
        result = self.a + self.b
        self.assertTrue(result == 30)

    def testsub(self):
        """sub"""
        result = self.a - self.b
        self.assertTrue(result == -10)
    def testmul(self):
        """mul"""
        result = self.a * self.b
        self.assertTrue(result == 24.747)
    def testdiv(self):
        """div"""
        result = self.a * self.b
        self.assertTrue(result == 5.3333)
if __name__ == '__main__':
    unittest.main()