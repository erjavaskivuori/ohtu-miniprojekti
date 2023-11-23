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


Print Citation List
	Input  listaa
	Run Application
	Output Should Contain  a, a, a


Adding Citation Gives Correct Prompts
	Input  lisää
	Run Application
	Output Should Contain  Syötä tyyppi:
	Output Should Contain  Syötä tekijä:
	Output Should Contain  Syötä otsikko:
	Output Should Contain  Syötä vuosi:


*** Keywords ***
Create Citation Article
	Input  lisää
	Input  article
	Input  Nimi Sukunimi
	Input  Otsikko on Aina Kiva Olla
	Input  2004
