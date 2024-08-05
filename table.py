import re
import os
import requests
import csv
from scraper import kolesar_scraper



def podatki_v_csv(directory, ime_datoteke, glavni_list):
    if os.path.exists(directory + "/" + ime_datoteke):
        os.remove(directory + "/" + ime_datoteke)
    fieldnames = list((glavni_list[0]).keys())
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, ime_datoteke)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(glavni_list)
    return 

