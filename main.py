import re
import os
import requests
import csv
from scraper import dobi_rank_po_sto
from scraper import dobi_kolesar_podatke

datum = "2024-08-04" # datum oblike XXXX-XX-XX

dobi_rank_po_sto(10, "Lestvica", datum)
dobi_kolesar_podatke(10, "Lestvica")

def podatki_v_csv():
    return