# Parameterizing of a test is done to run the test against multiple sets of inputs.
# We can do this by using the following marker −
#
# @pytest.mark.parametrize
import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output

# Here the test multiplies an input with 11 and compares the result with the expected output.
# The test has 4 sets of inputs, each has 2 values – one is the number to be multiplied with 11
# and the other is the expected result.
# Execute the test by running the following command −
# Pytest -k multiplication -v