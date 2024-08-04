import re
import os
import requests
import csv
from scraper import dobi_rank_po_sto
from scraper import dobi_list_podatkov


datum = "2024-08-04" # datum oblike XXXX-XX-XX

dobi_rank_po_sto(10, "Lestvica", datum)
glavni_list = dobi_list_podatkov(10, "Lestvica")

from table import podatki_v_csv

podatki_v_csv("Tabela", "kolesarji.csv", glavni_list)