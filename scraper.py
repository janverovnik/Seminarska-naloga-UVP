import requests
import re
import os

def get_hmtl_to_file(url, directory, ime_datoteke):
    try:
        niz = requests.get(url).text
    except requests.exceptions.RequestException:
        print("Preverite povezavo in poskusite znova.")
        return
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, ime_datoteke), "w", encoding="utf-8") as f:
        f.write(niz)
    return

def dobi_rank_po_sto(n):
    for i in range(n):
        offset = str(i * 100)
        offset_plus_ena = str(i * 100 + 1)
        offset_plus_sto = str((i + 1) * 100)
        pcs_url = f"https://www.procyclingstats.com/rankings.php?date=2024-07-29&nation=&age=&zage=&page=smallerorequal&team=&offset={offset}&active=&filter=Filter&p=me&s=all-time"
        get_hmtl_to_file(pcs_url, "Lestvica", f"{offset_plus_ena}-{offset_plus_sto}.html")
    return 

dobi_rank_po_sto(10)

