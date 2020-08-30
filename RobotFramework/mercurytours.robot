*** Settings ***
Documentation     Example test cases using the keyword-driven testing approach.
...
...               All tests contain a workflow constructed from keywords in
...               ``mercury_tours.py``. Creating new tests or editing
...               existing is easy even for people without programming skills.
...
...               The _keyword-driven_ appoach works well for normal test
...               automation, but the _gherkin_ style might be even better
...               if also business people need to understand tests. If the
...               same workflow needs to repeated multiple times, it is best
...               to use to the _data-driven_ approach.
Library           mercury_tours.py
*** Test Cases ***
Mercury Demo Tours Book Flight
    [Tags]  login    mercurydemotours
    ${driver} =  Initialiseddriver
    Launch URL   ${driver}   http://newtours.demoaut.com/
    Log    Navigate toMercury DemoTours
    Login   ${driver}   mercury   mercury
    Book Ticket  ${driver}
Advantage Online Shopping
    [Tags]   advantageshopping    shopping
    ${driver} =  Initialiseddriver
    Launch URL   ${driver}   http://advantageonlineshopping.com
    Log    Navigate to Advantage Online Shopping
    Quit    ${driver}
Flipkart Shopping
    [Tags]   flipkartshopping    shopping
    ${driver} =  Initialiseddriver
    Launch URL   ${driver}   http://flipkart.com
    Log    Navigate to Flipkart
    Quit    ${driver}
Demo
    [Tags]  demo
    should be equal as integers  1    1
    First keyword
    Verify Title
*** Keywords ***
First keyword
    Log   Demo of Tag1
    Log   Demo of Tag2
    Log   Demo of Tag3
    Log   Demo of Tag4
Verify Title
    ${title} =  Get Title
    should be equal as strings  ${title}    demo

