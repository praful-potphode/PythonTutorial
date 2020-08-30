*** Settings ***
Documentation    Suite description
Library          apitesting.py
*** Test Cases ***
LISTUSERS GET API
    [Tags]    DEBUG
    When "LISTUSERS" GET request is sent to "https://reqres.in" site
    Then Status code "200" is received

UPDATE USER PUT API
    [Tags]    DEBUG
    When "UPDATEUSER" PUT request is sent to "https://reqres.in" site
    Then Status code "200" is received
CREATE USER POST API
    [Tags]    DEBUG
    When "CREATEUSER" POST request is sent to "https://reqres.in" site
    Then Status code "201" is received
DELETE USER DELETE API
    [Tags]    DEBUG
    When "DELETEUSER" DELETE request is sent to "https://reqres.in" site for userid "8"
    Then Status code "204" is received
*** Keywords ***
"${APINAME}" DELETE request is sent to "${ENDPOINT}" site for userid "${USERID}"
    DELETE USER     ${APINAME}    ${ENDPOINT}    ${USERID}
"${APINAME}" POST request is sent to "${ENDPOINT}" site
    &{DATA}    create dictionary  name= testuser    job= ind resident
    UPDATE USER     ${APINAME}    ${ENDPOINT}    ${DATA}
"${APINAME}" GET request is sent to "${ENDPOINT}" site
    LIST USERS      ${APINAME}    ${ENDPOINT}
Status code "${STATUSCODE}" is received
    VERIFY STATUS CODE    ${STATUSCODE}
"${APINAME}" PUT request is sent to "${ENDPOINT}" site
    &{DATA}    create dictionary  name= morpheus1    job= zion resident
    UPDATE USER     ${APINAME}    ${ENDPOINT}    ${DATA}