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


Adding Article Gives Correct Prompts
	Input  lisää
	Input  2
	Run Application
	Output Should Contain  Syötä author:
	Output Should Contain  Syötä title:
	Output Should Contain  Syötä year:
	Output Should Contain  Syötä journaltitle:


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
	Input  2
	Input  Nimi Sukunimi
	Input  Otsikko on Aina Kiva Olla
	Input  2004
	Input  Joku journaltitle
