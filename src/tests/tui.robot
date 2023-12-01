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

Wrong Input Gives Correct Prompt In Main Menu
	Input  lop
	Run Application
	Output Should Contain  *** VIRHE: lop: tuntematon komento.

Adding Article Gives Correct Prompts
	Input  lisää
	Input  2
	Run Application
	Output Should Contain  Syötä tekijä (author):
	Output Should Contain  Syötä otsikko (title): 
	Output Should Contain  Syötä vuosi (year): 
	Output Should Contain  Syötä lehden nimi (journaltitle): 
	Output Should Contain  Haluatko lisätä tägin: 

Wrong Input Gives Correct Prompt In Add Citation Menu
	Input  lisää
	Input  viisi
	Run Application
	Output Should Contain  *** VIRHE: Syöte 'viisi' ei kelpaa.

Added Citation Can Be Found on Citation List
	Create Citation Article Without Tag
	Input  listaa
	Run Application
	Output Should Contain  Nimi Sukunimi
	Output Should Contain  Otsikko on Aina Kiva Olla

Added Citation With Tag Can Be Found on Citation List
	Create Citation Article With Tag
	Input  listaa
	Run Application
	Output Should Contain  Nimi Sukunimi
	Output Should Contain  Otsikko on Aina Kiva Olla
	Output Should Contain  2004
	Output Should Contain  Joku journaltitle
	Output Should Contain  tagi


Resetting Database Works
	Create Citation Article Without Tag
	Run Application
	Reset Database
	Input  listaa
	Run Application
	Output Should Not Contain  Nimi Sukunimi


*** Keywords ***
Create Citation Article Without Tag
	Input  lisää
	Input  2
	Input  Nimi Sukunimi
	Input  Otsikko on Aina Kiva Olla
	Input  2004
	Input  Joku journaltitle
	Input  ei

Create Citation Article With Tag
	Input  lisää
	Input  2
	Input  Nimi Sukunimi
	Input  Otsikko on Aina Kiva Olla
	Input  2004
	Input  Joku journaltitle
	Input  kyllä
	Input  tagi