*** Settings ***
Resource  resource.robot

*** Test Cases ***
Print Help Menu
	Input  menu
	Input  lopeta
	Run Application
	Output Should Contain  \nApu:\n

*** Keywords ***
Create Citation Article
	Input  lisää
	Input  article
	Input  Nimi Sukunimi
	Input  Otsikko on Aina Kiva Olla
	Input  2004
