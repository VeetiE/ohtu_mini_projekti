*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page



*** Test Cases ***
Input value to form
    Click Element  id:referenceType
    Set cite  testi
    Click Element  id:submit


*** Keywords ***
Go To Main Page
    Go To  ${HOME URL}

Set cite
    [Arguments]  ${cite}
    Input text  referenceType  ${cite}
