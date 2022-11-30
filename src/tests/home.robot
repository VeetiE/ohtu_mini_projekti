*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page


*** Test Cases ***
Main Page Should Be Open
    Title Should Be   Tulostus:


*** Keywords ***
Go To Main Page
    Go To  ${HOME URL}
