*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page



*** Test Cases ***

Form Creates A Correct Book
    Go To Main Page
    Click Element  id:refFormLink
    Click Element  id:submitButton
    Click Element  id:author
    Set author  testi
    Click Element  id:title
    Set title  Joe
    Click Element  id:publisher
    Set publisher  JoeProductions
    Click Element  id:address
    Set address  JoesBasement
    Click Element  id:year
    Set published  1995

    Click Element  id:createNew
    Title Should Be   BibTeX-viittaus generaattori
    Click Element  id:printBibtexLink
    
    Element Should Contain    xpath://div  @book{testi1995,reference_type="book",author="testi",title="Joe",publisher="JoeProductions",address="JoesBasement",year="1995",}



Form Creates A Correct Article
    Go To Main Page
    Click Element  id:refFormLink
    Select From List By Value  name:references  article
    Click Element  id:submitButton
    Click Element  id:author
    Set author  Hugh Highs
    Click Element  id:title
    Set title  High Highs Lower
    Click Element  id:journal
    Set journal  My Journal
    Click Element  id:year
    Set published  1995

    Click Element  id:createNew
    Title Should Be   BibTeX-viittaus generaattori
    Click Element  id:printBibtexLink
    
    Element Should Contain    xpath://div  @article{hughh1995,reference_type="article",author="Hugh Highs",title="High Highs Lower",journal="My Journal",year="1995",}








From Add A New Ref And Create Correct Cite
    Go To Main Page
    Click Element  id:addNewReferenceType
    Click Element  id:tyyppi
    Set tyyppi  video
    Select Checkbox  id:address
    Select Checkbox  id:author
    Click Element  id:submitButton
    Click Element  id:frontPageLink


*** Keywords ***
Go To Main Page
    Go To  ${HOME URL}

Go To Form Page
    Go To  ${FORM URL}

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
    [Arguments]  ${year}
    Input text  year  ${year}

Set publisher
    [Arguments]  ${publisher}
    Input text  publisher  ${publisher}    

Set address
    [Arguments]  ${address}
    Input text  address  ${address}    


Set journal
    [Arguments]  ${journal}
    Input text  journal  ${journal}    

Set tyyppi
    [Arguments]  ${tyyppi}
    Input text  tyyppi  ${tyyppi}    


