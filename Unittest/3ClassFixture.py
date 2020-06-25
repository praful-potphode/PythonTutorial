# TestCase class has a setUpClass() method which can be overridden to execute before the execution of individual tests
# inside a TestCase class. Similarly, tearDownClass() method will be executed after all test in the class. Both the
# methods are class methods. Hence, they must be decorated with @classmethod directive.
# The following example demonstrates the use of these class methods −

import unittest
class TestFixtures(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('called once before any tests in class')

    @classmethod
    def tearDownClass(cls):
        print('\ncalled once after all tests in class')

    def setUp(self):
        self.a = 10
        self.b = 20
        name = self.shortDescription()
        print('\n', name)

    def tearDown(self):
        print('\nend of test', self.shortDescription())

    def test1(self):
        """One"""
        result = self.a + self.b
        self.assertTrue(True)

    def test2(self):
        """Two"""
        result = self.a - self.b
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()