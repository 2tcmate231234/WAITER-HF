# Alprogramok

def beolvasas():
    adatok = []
    with open("adatok.txt", "r", encoding="UTF-8") as fm:
        for sor in fm:
            adatok.append(float(sor.strip()))
    return adatok

def szamitas(a):
    return sum(a)

def eldontes(osszegek):
    talalt_elso = False
    elso = None
    utolso = None

    for i in range(len(osszegek)):
        if osszegek[i] > 10:
            if not talalt_elso:
                talalt_elso = True
                elso = i
            utolso = i
    if talalt_elso:
        return elso, utolso
    else:
        return -1, -1

def ot_fontos_fizetes(osszegek):
    for osszeg in osszegek:
        if osszeg % 5 != 0:
            return False
    return True

def osszes_bevetel(osszegek):
    osszeg = sum(osszegek)
    return osszeg + 0.5 * len(osszegek)


def kiir(elso, utolso,ossz,ö_f,ossz_bev):
    print(osszegek)
    print(fizetett)
    print(pennyk)
    print(f"{szmlt_penny}")
    print(otosok)
    print(maximalis)
    print(_8_23_val)
    print(kilenc_i)
    print(f"Az óra végen {osszegzes} lett a pénztárcájá-ban")
    if elso != -1:
        print(f"Az első tíz fontnál többet fizető vendég a, {elso + 1}  volt.")
        print(f"Az utolsó tíz fontnál többet fizető vendég a, {utolso + 1} volt.")
    if ot_fontos_fizetes(osszegek):
         print("Minden vendég csupa ötfontossal fizetett.")
    else:
         print("Volt olyan vendég, aki nem csak ötfontossal fizetett.")
    print(f"A nap végén a pincér {bevetel} fontot kapott")



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

# Fő program

# 1 input
osszegek = beolvasas()

# 2 Számítás
osszegzes = szamitas(osszegek)
elso, utolso = eldontes(osszegek)
ot_font=ot_fontos_fizetes(osszegek)
bevetel=osszes_bevetel(osszegek)
osszegek=beolvasas()
fizetett=pincerfizet(osszegek)
pennyk=kapott_penny(osszegek)
szmlt_penny=penny_szmll(osszegek)
otosok=legalabb_5(osszegek)
maximalis=legnagyobb_szamla(osszegek)
_8_23_val=_8_23_val_sum(osszegek)
kilenc_i=i_fizet_9(osszegek)


# 3 output
kiir(elso, utolso,osszegzes,ot_font,bevetel)