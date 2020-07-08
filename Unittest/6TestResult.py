# TestResult Class
# This class is used to compile information about the tests that have been successful and the tests that have met failure.
# A TestResult object stores the results of a set of tests.A TestResult instance is returned by the TestRunner.run() method.
#
# TestResult  instances have the following attributes −
#
# 1 Errors
# A list containing 2 - tuples of TestCase instances and strings holding formatted tracebacks.Each tuple represents
# a test which raised an unexpected exception.
#
# 2 Failures
# A list containing 2 - tuples of TestCase instances and strings holding formatted tracebacks.Each tuple represents
# a test where a failure was explicitly signalled using the TestCase.assert *() methods.
#
# 3 Skipped
# A list containing 2 - tuples of TestCase instances and strings holding the reason for skipping the test.
#
# 4 wasSuccessful()
# Return True if all tests run so far have passed, otherwise returns False.
#
# 5 stop()
# This method can be called to signal that the set of tests being run should be aborted.
#
# 6 startTestRun()
# Called once before any tests are executed.
#
# 7 stopTestRun()
# Called once after all tests are executed.
#
# 8 testsRun
# The total number of tests run so far.
#
# 9 Buffer
# If set to true, sys.stdout and sys.stderr will be buffered in between startTest() and stopTest() being called.
import unittest

from unittest.test import suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    result = runner.run(test_suite)

    print(
    "---- START OF TEST RESULTS")
    print(    result)

    print(
    "result::errors")
    print(
    result.errors)

    print(
    "result::failures")
    print(
    result.failures)

    print(
    "result::skipped")
    print(
    result.skipped)

    print(
    "result::successful")
    print(
    result.wasSuccessful())

    print(
    "result::test-run")
    print(
    result.testsRun)
    print(
    "---- END OF TEST RESULTS")