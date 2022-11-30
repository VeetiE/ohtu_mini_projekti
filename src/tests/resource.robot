*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0.2 seconds
${HOME URL}  http://${SERVER}
${FORM URL}  http://${SERVER}/referenceForm

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Home Page Should Be Open
    Title Should Be  Etusivu

