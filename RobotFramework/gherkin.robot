*** Settings ***
Force Tags  REGRESSION
Default Tags     SMOKE
Documentation     Example test case using the gherkin syntax.
...
...               This test has a workflow similar to the keyword-driven
...               examples. The difference is that the keywords use higher
...               abstraction level and their arguments are embedded into
...               the keyword names.
...
...               This kind of _gherkin_ syntax has been made popular by
...               [http://cukes.info|Cucumber]. It works well especially when
...               tests act as examples that need to be easily understood also
...               by the business people.
Library           mercury_tours.py
Suite Setup    Before Suite
Suite Teardown    After Suite
Test Setup    Load Test Data ${TEST NAME}
*** Test Cases ***
#Addition
#    Given calculator has been cleared
#    When user types "1 + 1"
#    and user pushes equals
#    Then result is "2"
Flipkart BDD
    [TAGS]  FLIPKART
    [Documentation]  testing
    Given browser is launched
    When user launches "http://flipkart.com" page
    Then page should be launched
AdvantageOnline Shopping BDD
    Given browser is launched
    When user launches "http://advantageonlineshopping.com" page
    Then page should be launched
*** Keywords ***
browser is launched
    ${driver} =  Initialiseddriver
    set global variable     ${driver}
user launches "${URL}" page
    Launch URL   ${driver}    ${URL}
page should be launched
    Log    Navigate to Site
#Calculator has been cleared
#    Push button    C
#User types "${expression}"
#    Push buttons    ${expression}
#
#User pushes equals
#    Push button    =
#
#Result is "${result}"
#    Result should be    ${result}
