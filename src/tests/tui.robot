*** Settings ***
Resource  resource.robot

*** Test Cases ***
Application Starts
	Run Application
	Output Should Contain  TERVETULOA


Menu Prompt Is Shown
	Run Application
	Output Should Contain  Komento (apu: syötä menu):


Print Help Menu
	Input  menu
	Run Application
	Output Should Contain  Apu:


Adding Citation Gives Correct Prompts
	Input  lisää
	Run Application
	Output Should Contain  Syötä tyyppi:
	Output Should Contain  Syötä tekijä:
	Output Should Contain  Syötä otsikko:
	Output Should Contain  Syötä vuosi:


Added Citation Can Be Found on Citation List
	Create Citation Article
	Input  listaa
	Run Application
	Output Should Contain  Nimi Sukunimi
	Output Should Contain  Otsikko on Aina Kiva Olla


Resetting Database Works
	Create Citation Article
	Run Application
	Reset Database
	Input  listaa
	Run Application
	Output Should Not Contain  Nimi Sukunimi


*** Keywords ***
Create Citation Article
	Input  lisää
	Input  article
	Input  Nimi Sukunimi
	Input  Otsikko on Aina Kiva Olla
	Input  2004
