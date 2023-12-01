# Ohtu miniprojekti
![GHA workflow badge](https://github.com/erjavaskivuori/ohtu-miniprojekti/workflows/CI/badge.svg)

[Testikattavuusraportti](https://github.com/erjavaskivuori/ohtu-miniprojekti/blob/main/testikattavuus.png)

[Product backlog ja sprint backlog](https://docs.google.com/spreadsheets/d/1TeniUNzDz5KInh-D-tHVcKsYnXuUdVKj35sreIyCLF8/edit?usp=sharing)

[Retrospektiivi](https://github.com/erjavaskivuori/ohtu-miniprojekti/blob/main/src/retro.md)

## Käyttöohjeet
1. Ohjelma toimii komentorivillä. Sinulla tulee olla asennettuna [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) ja vähintään [Python](https://www.python.org/downloads/) 3.10.
2. Kloonaa komentorivin komennolla `git clone git@github.com:erjavaskivuori/ohtu-miniprojekti.git` ohjelma haluttuun paikkaan.
3. Asenna riippuvuudet komennolla `poetry install`
4. Suorita tietokannan alustus komennolla `python3 ohtu-miniprojekti/src/build.py`
5. Suorita python ohjelma komennolla `python3 ohtu-miniprojekti/src/app.py`
6. Ohjelma antaa kaikki ohjeet viitteiden hallintaan. Käskyillä `menu`, `apua` tai `auta` saat kaikki komennot näkyviin.

## Definition of done

- User storyn mukainen toiminnallisuus toteutettu
- Yksikkötestaus tehty ja muotoilu tarkistettu (pylint)
- Dokumentoitu (docstring, asennusohjeet, käyttöohjeet)
- Integroitu ja testattu CI-palvelimella

[Lisenssi](https://github.com/erjavaskivuori/ohtu-miniprojekti/blob/main/LICENSE.md)
