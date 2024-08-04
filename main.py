import re
import os
import requests
import csv
from scraper import dobi_rank_po_sto
from scraper import dobi_list_podatkov
from scraper import izlusci_kolesar_url

datum = "2024-08-04" # datum oblike XXXX-XX-XX

dobi_rank_po_sto(10, "Lestvica", datum)
glavni_list = dobi_list_podatkov(10, "Lestvica")

def podatki_v_csv(directory, filename):
    fieldnames = list(izlusci_kolesar_url("Lestvica/1-100.html")[0].keys())
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        csv.DictWriter

    return