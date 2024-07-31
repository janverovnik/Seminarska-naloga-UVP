import requests
import re
import os

def get_html_to_file(url, directory, ime_datoteke):
    try:
        niz = requests.get(url).text
    except requests.exceptions.RequestException:
        print("Preverite povezavo in poskusite znova.")
        return
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, ime_datoteke), "w", encoding="utf-8") as f:
        f.write(niz)
    return

def dobi_rank_po_sto(n, directory, datum): # datum oblike XXXX-XX-XX (npr. 2024-07-31) kot string
    for i in range(n):
        offset = str(i * 100)
        offset_plus_ena = str(i * 100 + 1)
        offset_plus_sto = str((i + 1) * 100)
        pcs_url = f"https://www.procyclingstats.com/rankings.php?date={datum}&nation=&age=&zage=&page=smallerorequal&team=&offset={offset}&active=&filter=Filter&p=me&s=all-time"
        get_html_to_file(pcs_url, directory, f"{offset_plus_ena}-{offset_plus_sto}.html")
    return 

# dobi_rank_po_sto(10, "Podatki", "2024-07-31")


def izlusci_kolesar_url(ime_datoteke):
    with open(ime_datoteke, "r", encoding="utf-8") as f:
        niz = f.read()
    vzorec = r'<a    href="(rider/.*?)">'
    stevec = 0
    list1 = []
    for i in [pojavitev.group(1) for pojavitev in re.finditer(vzorec, niz)]:
        if stevec % 2 == 0:
            list1.append(i)
        stevec += 1
    return list1

# print(izlusci_kolesar_url("Podatki/1-100.html"))   


def dobi_kolesarja(n, directory1): # n, directory1 morata biti enaka kot n, directory pri dobi_rank_po_sto
    # os.makedirs(directory1, exist_ok=True)
    stevec = 1
    for i in range(n):
        prvi_del = str(i * 100 + 1)
        drugi_del = str((i + 1) * 100)
        directory2 = f"{prvi_del}-{drugi_del}"
        list1 = izlusci_kolesar_url(f"{directory1}/{prvi_del}-{drugi_del}.html")
        for url in list1:
            get_html_to_file("https://www.procyclingstats.com/" + url, directory2, f"{stevec}.-{url[6:]}.html")
            stevec += 1
    return        
    

# dobi_kolesarja(10, "Podatki")