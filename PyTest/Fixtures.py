# Fixtures are functions, which will run before each test function to which it is applied.
# Fixtures are used to feed some data to the tests such as database connections, URLs to test and some sort of input data.
# Therefore, instead of running the same code for every test, we can attach fixture function to the tests
# and it will run and return the data to the test before executing each test.
#
# A function is marked as a fixture by −
# @pytest.fixture
#
# A test function can use a fixture by mentioning the fixture name as an input parameter.
import pytest

@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0

# Here, we have a fixture function named input_value, which supplies the input to the tests.
# To access the fixture function, the tests have to mention the fixture name as input parameter.
#
# Pytest while the test is getting executed, will see the fixture name as input parameter.
# It then executes the fixture function and the returned value is stored to the input parameter, which can be used by the test.
#
# Execute the test using the following command −
# pytest -k divisible -v
