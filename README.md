# Ohtu miniprojekti
![GHA workflow badge](https://github.com/erjavaskivuori/ohtu-miniprojekti/workflows/CI/badge.svg)[![codecov](https://codecov.io/github/erjavaskivuori/ohtu-miniprojekti/graph/badge.svg?token=BJ1NFKVKDF)](https://codecov.io/github/erjavaskivuori/ohtu-miniprojekti)

## Asennusohjeet
- Asenna koneelle ajantasaiset versiot [SQLite](https://www.sqlite.org/) ja [poetry](https://python-poetry.org/) -ohjelmista, sekä niiden riippuvuudet (poetry 1.7.1 ja SQlite 3.40.1 sekä niitä uudemmat yhteensopivat versiot toiminevat)
- Hae uusin asennuspaketti [täältä](https://github.com/erjavaskivuori/ohtu-miniprojekti/releases/latest)
- Pura lataamasi paketti esim: `tar xfz viikko9.tar.gz`
- Avaa terminaali juuri puretussa kansiossa (esim ohtu-miniprojekti-viikko9)
- Suorita riippuvuuksien asennus komennolla: `PYTHON_KEYRING_BACKEND=keyring.backends.fail.Keyring poetry install --without dev --no-root`
- Alusta tietokonata komennolla: `poetry run python3 src/db/build.py`
- Lisää demodataa tietokantaan komennolla: `poetry run python3 src/db/populate.py`

## Käyttöohjeet
- Ohjelma käynnistetään projektin juurikansiossa (esim ohtu-miniprojekti-viikko9) komennolla: `poetry run python3 src/app.py`
- Ohjelman käyttöohjeet löytyvät itse ohjelmasta komentamalla `menu` päävalikossa, joka avautuu heti ohjelman käynnistymisen jälkeen.
- Muutokset viiteluetteloon tallentuvat heti ja pysyvästi.
- Luodut BiBTeX (.bib) -tiedostot löytyvät hakemistosta `bibtex_files`.

[Lisenssi](https://github.com/erjavaskivuori/ohtu-miniprojekti/blob/main/LICENSE.md)

## Kehitystyö

- [Product backlog ja sprint backlog](https://docs.google.com/spreadsheets/d/1TeniUNzDz5KInh-D-tHVcKsYnXuUdVKj35sreIyCLF8/edit?usp=sharing)

- [2. Sprintin retrospektiivi](https://github.com/erjavaskivuori/ohtu-miniprojekti/blob/main/retro_2.md)

- [3. Sprintin retrospektiivi](https://github.com/erjavaskivuori/ohtu-miniprojekti/blob/main/retro_3.md)

### Definition of done
- User storyn mukainen toiminnallisuus toteutettu
- Yksikkötestaus tehty ja muotoilu tarkistettu (pylint)
- Dokumentoitu (docstring, asennusohjeet, käyttöohjeet)
- Integroitu ja testattu CI-palvelimella


