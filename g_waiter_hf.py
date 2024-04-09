def beolvasas():
    osszegek=[]
    with open("adatok.txt", "r", encoding="UTF-8") as fm:
        for sor in fm:
            osszegek.append(float(sor.strip()))
    return osszegek

def pincerfizet(l):
    fizetett=False
    for elem in l:
        if elem<0:
            fizetett=True
    return fizetett
        
def kapott_penny(l):
    kapott=False
    for elem in l:
        if elem!=int(elem):
            kapott=True
    return kapott
    
def penny_szmll(l):
    szum=0
    for elem in l:
        szum+=elem-int(elem)
    return int(100*szum)
    
def legalabb_5(l):
    db=0
    for elem in l:
        if elem>=5:
            db+=1
    return db

def legnagyobb_szamla(l):
    return max(l)

def _8_23_val_sum(l):
    return 8.23+sum(l)

def i_fizet_9(l):
    i=0
    while i<len(l) and l[i]!=9:
        i+=1
    return i+1

osszegek=beolvasas()
fizetett=pincerfizet(osszegek)
pennyk=kapott_penny(osszegek)
szmlt_penny=penny_szmll(osszegek)
otosok=legalabb_5(osszegek)
maximalis=legnagyobb_szamla(osszegek)
_8_23_val=_8_23_val_sum(osszegek)
kilenc_i=i_fizet_9(osszegek)

print(osszegek)
print(fizetett)
print(pennyk)
print(f"{szmlt_penny}")
print(otosok)
print(maximalis)
print(_8_23_val)
print(kilenc_i)