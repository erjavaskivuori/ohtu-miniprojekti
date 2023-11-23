*** Settings ***
Resource  resource.robot

*** Test Cases ***
Print Help Menu
	Input  menu
	Input  lopeta
	Run Application
	Output Should Contain  \nApu:\n


Print Citation List
	Input  listaa
	input  lopeta
	Run Application
	Output Should Contain  lista kaikista

*** Keywords ***
Create Citation Article
	Input  lisää
	Input  article
	Input  Nimi Sukunimi
	Input  Otsikko on Aina Kiva Olla
	Input  2004
