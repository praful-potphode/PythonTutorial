# In a real scenario, once a new version of the code is ready to deploy,
# # it is first deployed into pre-prod/ staging environment.
# # Then a test suite runs on it.
# #
# # The code is qualified for deploying to production only if the test suite passes.
# # If there is test failure, whether it is one or many, the code is not production ready.
# #
# # Therefore, what if we want to stop the execution of test suite soon after n number of test fails.
# # This can be done in pytest using maxfail.
# #
# # The syntax to stop the execution of test suite soon after n number of test fails is as follows −
# #
# # pytest --maxfail = <num>

import pytest
import math

def test_sqrt_failure():
   num = 25
   assert math.sqrt(num) == 6

def test_square_failure():
   num = 7
   assert 7*7 == 40

def test_equality_failure():
   assert 10 == 11

# All the 3 tests will fail on executing this test file.
# Here, we are going to stop the execution of the test after one failure itself by −
#
# pytest test_failure.py -v --maxfail = 1
# pytest -v maxfaildemo.py --maxfail=2
