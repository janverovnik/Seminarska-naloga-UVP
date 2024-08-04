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

def dobi_rank_po_sto(n, directory, datum): # datum oblike XXXX-XX-XX kot string (npr. "2024-07-31") 
    for i in range(n):
        offset = str(i * 100)
        offset_plus_ena = str(i * 100 + 1)
        offset_plus_sto = str((i + 1) * 100)
        pcs_url = f"https://www.procyclingstats.com/rankings.php?date={datum}&nation=&age=&zage=&page=smallerorequal&team=&offset={offset}&active=&filter=Filter&p=me&s=all-time"
        get_html_to_file(pcs_url, directory, f"{offset_plus_ena}-{offset_plus_sto}.html")
    return 

# dobi_rank_po_sto(1, "Lestvica", "2024-08-04")


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

# print(izlusci_kolesar_url("Lestvica/1-100.html"))   
def stevilo_zmag_grand_tour(niz):
    zmage_posameznih_tour = len(re.findall(r'">&nbsp; <span class="shirt st4 w14"></span></div><div><span class="blue">GC</span> <a href="race/tour-de-france/\d+/gc">', niz))
    zmage_posameznih_giro = len(re.findall(r'">&nbsp; <span class="shirt st4 w14"></span></div><div><span class="blue">GC</span> <a href="race/giro-d-italia/\d+/gc">', niz))
    zmage_posameznih_vuelta = len(re.findall(r'">&nbsp; <span class="shirt st4 w14"></span></div><div><span class="blue">GC</span> <a href="race/vuelta-a-espana/\d+/gc">', niz))
    zmage_posameznih_gt = zmage_posameznih_giro + zmage_posameznih_tour + zmage_posameznih_vuelta
    zmage_tour = re.search(r'(\d+)x</b>&nbsp;<span class="shirt st4 w14"></span></div><div><span class="blue">GC</span> <a href="race/tour-de-france/\d+/gc">Tour de France</a>', niz)
    zmage_giro = re.search(r'(\d+)x</b>&nbsp;<span class="shirt st4 w14"></span></div><div><span class="blue">GC</span> <a href="race/giro-d-italia/\d+/gc">Giro d\'Italia</a>', niz)
    zmage_vuelta = re.search(r'(\d+)x</b>&nbsp;<span class="shirt st4 w14"></span></div><div><span class="blue">GC</span> <a href="race/vuelta-a-espana/\d+/gc">La Vuelta ciclista a España</a>', niz)
    if zmage_tour != None:
        tour = zmage_tour.group(1)
    else:
        tour = 0
    if zmage_giro != None:
        giro = zmage_giro.group(1)
    else:
        giro = 0
    if zmage_vuelta != None:
        vuelta = zmage_vuelta.group(1)
    else:
        vuelta = 0
    return str(int(tour) + int(giro) + int(vuelta) + zmage_posameznih_gt)

def stevilo_zmag_spomenik(niz):
    RBX_pos = len(re.findall(r'">&nbsp; </div><div><span class="blue"></span> <a href="race/paris-roubaix/\d+/result">', niz))
    MSR_pos = len(re.findall(r'">&nbsp; </div><div><span class="blue"></span> <a href="race/milano-sanremo/\d+/result">', niz))
    RVV_pos = len(re.findall(r'">&nbsp; </div><div><span class="blue"></span> <a href="race/ronde-van-vlaanderen/\d+/result">', niz))
    LBL_pos = len(re.findall(r'">&nbsp; </div><div><span class="blue"></span> <a href="race/liege-bestogne-liege/\d+/result">', niz))
    LOM_pos = len(re.findall(r'">&nbsp; </div><div><span class="blue"></span> <a href="race/il-lombardia/\d+/result">', niz))
    posamezni = RBX_pos + MSR_pos + RVV_pos + LBL_pos + LOM_pos
    RBX = re.search(r'(\d+)x</b>&nbsp;</div><div><span class="blue"></span> <a href="race/paris-roubaix/\d+/result">', niz)
    MSR = re.search(r'(\d+)x</b>&nbsp;</div><div><span class="blue"></span> <a href="race/milano-sanremo/\d+/result">', niz)
    RVV = re.search(r'(\d+)x</b>&nbsp;</div><div><span class="blue"></span> <a href="race/ronde-van-vlaanderen/\d+/result">', niz)
    LBL = re.search(r'(\d+)x</b>&nbsp;</div><div><span class="blue"></span> <a href="race/liege-bastogne-liege/\d+/result">', niz)
    LOM = re.search(r'(\d+)x</b>&nbsp;</div><div><span class="blue"></span> <a href="race/il-lombardia/\d+/result">', niz)
    if RBX != None:
        RBX = RBX.group(1)
    else:
        RBX = 0
    if MSR != None:
        MSR = MSR.group(1)
    else:
        MSR = 0
    if RVV != None:
        RVV = RVV.group(1)
    else:
        RVV = 0
    if LBL != None:
        LBL = LBL.group(1)
    else:
        LBL = 0
    if LOM != None:
        LOM = LOM.group(1)
    else:
        LOM = 0
    neposamezni = int(RBX) + int(MSR) + int(RVV) + int(LBL) + int(LOM)
    return str(posamezni + neposamezni)
    

    




def kolesar_scraper(niz): 
    alltime = re.search(r'All time</a></div><div class=" rnk"  >(\d+)</div>', niz)
    ime = re.search(r'<title>(.+)</title>', niz)
    drzava = re.search(r'"nation/.+">(.+)</a><br />(<span>)?<b>', niz)
    oneday = re.search(r'<div class="bg green" style="width: \d+(\.\d+)?%; height: 100%;  "></div></div><div class="pnt">(\d+)', niz)
    GC = re.search(r'<div class="bg red" style="width: \d+(\.\d+)?%; height: 100%;  "></div></div><div class="pnt">(\d+)', niz)
    TT = re.search(r'<div class="bg blue" style="width: \d+(\.\d+)?%; height: 100%;  "></div></div><div class="pnt">(\d+)', niz)
    sprint = re.search(r'<div class="bg orange" style="width: \d+(\.\d+)?%; height: 100%;  "></div></div><div class="pnt">(\d+)', niz)
    climb = re.search(r'<div class="bg purple" style="width: \d+(\.\d+)?%; height: 100%;  "></div></div><div class="pnt">(\d+)', niz)
    hills = re.search(r'<div class="bg pink" style="width: \d+(\.\d+)?%; height: 100%;  "></div></div><div class="pnt">(\d+)', niz)
    st_zmag = re.search(r'<ul class="rider-kpi"  style=" "><li class="" ><div class=" nr"  >(\d+)</div>', niz)
    struktura_zmag = re.search(r'Wins</a></div><div class=" info fs11"  >GC \((\d+)\)</div><div class=" info fs11"  >Oneday races \((\d+)\)</div><div class=" info fs11"  >ITT \((\d+)\)</div>', niz)
    st_zac_grand_tour = re.search(r'<li class="" ><div class=" nr"  >(\d+)</div><div class=" title"  ><a    href="rider/.+/statistics/grand-tour-starts">Grand tours', niz)
    st_zmag_grand_tour = stevilo_zmag_grand_tour(niz)
#   struktura_grand_tour = re.search(r'Grand tours</a></div><div class=" info fs11"  >tour \((\d+)\) giro \((\d+)\) vuelta\((\d+)\)', niz)
    st_zac_spomenik = re.search(r'<li class="" ><div class=" nr"  >(\d+)</div><div class=" title"  ><a    href="rider/.+/statistics/top-classic-results">Classics', niz)
    st_zmag_spomenik = stevilo_zmag_spomenik(niz)
#   struktura_zac_klasik = re.search(r'Classics</a></div><div class=" info fs11"  >RBX\((\d+)\)</div><div class=" info fs11"  >MSR\((\d+)\)</div><div class=" info fs11"  >RVV\((\d+)\)</div><div class=" info fs11"  >LBL\((\d+)\)</div><div class=" info fs11"  >LOM\((\d+)\)', niz)
    st_sezon = str(len([i for i in re.finditer(r'<tr ><td class="season  " >\d+</td><td class="bar  " >', niz)]))
    etapne_zmage = str(int(st_zmag.group(1)) - int(struktura_zmag.group(1)) - int(struktura_zmag.group(2)) - int(struktura_zmag.group(3)))
    return {"ime": ime.group(1)[:-1], "drzava": drzava.group(1), "rang": alltime.group(1) + ".", "sezone": st_sezon, "t_enodnevne": oneday.group(2), "t_GC": GC.group(2),"t_kronometer": TT.group(2), "t_sprint": sprint.group(2), "t_gore": climb.group(2), "t_hribi": hills.group(2), "zmage": st_zmag.group(1), "etapne": etapne_zmage, "GC": struktura_zmag.group(1), "enodnevne": struktura_zmag.group(2), "kronometer": struktura_zmag.group(3), "grand tour zac.": st_zac_grand_tour.group(1), "grand tour zmage": st_zmag_grand_tour,  "spomeniki zac.": st_zac_spomenik.group(1), "spomeniki zmage": st_zmag_spomenik}

#niz = requests.get("https://www.procyclingstats.com/rider/sean-kelly").text
#print(kolesar_scraper(niz))
#print(stevilo_zmag_grand_tour(niz))
#print(stevilo_zmag_spomenik(niz))

def dobi_kolesar_podatke(n, directory1): # n, directory1 morata biti enaka kot n, directory pri dobi_rank_po_sto
    glavni_list = [] # ta je zdele messy
    for i in range(n):
        prvi_del = str(i * 100 + 1)
        drugi_del = str((i + 1) * 100)
        directory2 = f"{prvi_del}-{drugi_del}"
        list1 = izlusci_kolesar_url(f"{directory1}/{prvi_del}-{drugi_del}.html")
        for url in list1:
            try:
                niz = requests.get("https://www.procyclingstats.com/" + url).text
            except requests.exceptions.RequestException:
                print("Preverite povezavo in poskusite znova.")
            glavni_list.append(kolesar_scraper(niz))
#            print(glavni_list)
    return glavni_list       
    

# print(dobi_kolesar_podatke(1, "Lestvica"))


            
        
        