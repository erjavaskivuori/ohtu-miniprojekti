
# Näin että stringit aina mätsäävät eikä kirjoitusvirhe
# esimerkiksi failaa testejä
class MSG:
    not_implemented = "Komentoa ei ole implementoitu"

    class Bib:
        create_ok = "Tiedosto luotu onnistuneesti"
        create_fail = "Tiedoston luonti epäonnistui \
(tarkista oikeudet tai käytitkö kiellettyjä merkkejä)"
        ask_filename = "tiedoston nimi (.bib)"

    class Tag:
        fail_empty = "sinulla ei ole vielä yhtään sitaattia"
        fail_unknown = "Antamaasi id:tä ei ole olemassa"
        fail_retag = "Sitaatilla on jo tägi"
        success = "Tägi lisätty onnistuneesti"
        info_list = "Lista kaikista sitaateistasi:"
        info_taglist = "Lista kaikista sitaateistasi:"
        ask_for_id = "sen sitaatin id, jolle haluat lisätä tägin"
        ask_tag = "jokin yllä olevista tägeista tai uusi tägi"
        ask_new_tag = "uusi tägi"

    class Add:
        ask_label = "tunniste"
        ask_type = "tyypin numero, vaihtoehtoja ovat Kirja (1), Artikkeli (2) \
ja Inproceedings (3)"
        ask_tag = "tägi"
        ask_add_tag = "Lisätäänkö tägi (kyllä/ei)"
        success = "Viite lisätty onnistuneesti"
        fail = "Viitten lisäys ei onnistunut"
        info_label_in_use = "Tunniste on jo käytössä"

    class Drop:
        ask_sure = "Oletko ihan varma (kyllä/ei)"
        success = "Viitteet tyhjennetty."
        aborted = "Tyhjennys peruutettu."

    class Delete:
        ask_id = "sitaatin id"
        success = "Viite poistettu"
        fail = "Viitteen poisto ei onnistunut"

    class List:
        empty = "Viitteitä ei löydy."

    class Search:
        ask_tag = "tägi"
