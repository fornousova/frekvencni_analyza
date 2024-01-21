from itertools import zip_longest

def frekvence_pismen(soubor):
    try:
        with open(soubor, 'r', encoding='utf-8') as soubor:
            text = soubor.read()

            # Vytvoření slovníku pro frekvenci písmen v textu
            frekvence_pismen = {}
            for pismeno in text:
                if pismeno.isalpha():
                    frekvence_pismen[pismeno] = frekvence_pismen.get(pismeno, 0) + 1

            # Seřazení písmen podle frekvence sestupně
            serazena_pismena = sorted(frekvence_pismen.items(), key=lambda x: x[1], reverse=True)

            # Vytvoření listu seřazených písmen
            serazeny_list = [pismeno for pismeno, pocet in serazena_pismena]

            return serazeny_list

    except FileNotFoundError:
        print(f"Chyba: Soubor '{soubor}' nenalezen.")
    except Exception as e:
        print(f"Došlo k chybě: {e}")

def slovnik_z_listu(list1, list2, hodnota=' '):
    # Vytvoření slovníku spojenim listů
    result_slovnik = dict(zip_longest(list1, list2, fillvalue=hodnota))
    return result_slovnik

def desifruj_se_slovnikem(soubor_cesty, frekvencni_slovnik, finalni_slovnik=None, hodnota=' '):
    try:
        with open(soubor_cesty, 'r', encoding='utf-8') as soubor:
            zasifrovany_text = soubor.read()

            # Vytvoření slovníku pro dešifrování
            substitucni_slovnik = slovnik_z_listu(frekvencni_slovnik, list('abcdefghijklmnopqrstuvwxyz'), hodnota)

            # Přidání finálního slovníku (pokud existuje)
            if finalni_slovnik:
                substitucni_slovnik.update(finalni_slovnik)

            # Dešifrování textu pomocí substitučního slovníku
            desifrovany_text = ''.join(substitucni_slovnik.get(pismeno, pismeno) for pismeno in zasifrovany_text)

            return desifrovany_text

    except FileNotFoundError:
        print(f"Chyba: Soubor '{soubor_cesty}' nenalezen.")
    except Exception as e:
        print(f"Došlo k chybě: {e}")

# Cesty k souborům
anglicky_text = 'sherlock-holmes.txt'
zasifrovany_text = 'sifrovany_text.txt'

# Analyzuje frekvenci písmen v anglickém textu
frekvencni_slovnik = frekvence_pismen(anglicky_text)

# Vytvoří slovník pro dešifrování
desifrovany_text = desifruj_se_slovnikem(zasifrovany_text, frekvencni_slovnik)

# Příklad použití finálního slovníku
finalni_slovnik = {'p': 'e', 'y': 't', 'q': 'a', 'b': 'o', 'c': 'i', 'k': 'h', 'l': 'n', 't': 's', 'a': 'r', 'm': 'd', 'n': 'l', 'f': 'u', 'v': 'w', 'i': 'g', 
'x': 'c', 'j': 'y', 'o': 'm', 'r': 'f', 'e': 'p', 'z': 'b', 'w': 'k', 'g': 'v', 'd': 'q', 'h': 'q', 'u': 'j', 's': 'z'}

# Použije finální slovník pro dešifrování
desifrovany_text_s_finalnim_slovnikem = desifruj_se_slovnikem(zasifrovany_text, frekvencni_slovnik, finalni_slovnik)

print(desifrovany_text_s_finalnim_slovnikem)
