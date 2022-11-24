*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page



*** Test Cases ***
Input value to form
    Click Element  id:referenceType
    Set cite  testi
    Click Element  id:title
    Set title  testi
    Click Element  id:author
    Set author  testi
    Click Element  id:published
    Set published  5
    
    Click Element  id:submit

*** Keywords ***
Go To Main Page
    Go To  ${HOME URL}

Set cite
    [Arguments]  ${cite}
    Input text  referenceType  ${cite}

Set title
    [Arguments]  ${title}
    Input text  title  ${title}

Set author
    [Arguments]  ${author}
    Input text  author  ${author}

Set published
    [Arguments]  ${published}
    Input text  published  ${published}
