*** Settings ***
Resource  resource.robot
Library  String

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
	Output Should Contain  Komennot:

Wrong Input Gives Correct Prompt In Main Menu
	Input  lop
	Run Application
	Output Should Contain  VIRHE: lop: tuntematon komento.

Adding Article Gives Correct Prompts
	Input  lisää
	${Label} =    Create Random Label
	Input  ${Label}
	Input  2
	Run Application
	Output Should Contain  Syötä tekijä (author):
	Output Should Contain  Syötä otsikko (title): 
	Output Should Contain  Syötä vuosi (year): 
	Output Should Contain  Syötä lehden nimi (journaltitle): 
	Output Should Contain  Lisätäänkö tägi (kyllä/ei): 

Wrong Input Gives Correct Prompt In Add Citation Menu
	Input  lisää
	Input  Create Random Label
	Input  viisi
	Run Application
	Output Should Contain  VIRHE: Syöte 'viisi' ei kelpaa.

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

# Käyttäjänä haluan mahdollisuuden generoida järjestelmässä 
# olevista viitteistä LaTeX-dokumenttiin sopivan BibTeX-muotoisen tiedoston
Create BibTex File From Citation
    input  luo
	input  tiedoston_nimi
	Run Application
	Output Should Contain  Tiedosto luotu onnistuneesti

# Käyttäjänä haluan pystyä hakemaan viitteitä tagilla.
Create Citation Article With Tag
	Create Citation Article With Tag
	Input  listaa
	Run Application
	Output Should Contain  Nimi Sukunimi
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
	${Label} =  Create Random Label
	Input  ${Label}
	Input  2
	Input  Nimi Sukunimi
	Input  Otsikko on Aina Kiva Olla
	Input  2004
	Input  Joku journaltitle
	Input  ei

Create Citation Article With Tag
	Input  lisää
	${Label} =  Create Random Label
	Input  ${Label}
	Input  2
	Input  Nimi Sukunimi
	Input  Otsikko on Aina Kiva Olla
	Input  2004
	Input  Joku journaltitle
	Input  kyllä
	Input  tagi

Create Random Label
    ${RANUSER}    Generate Random String    10    [LETTERS]
    [Return]    ${RANUSER}