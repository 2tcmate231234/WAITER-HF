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
    
def kiir(elso, utolso,ossz):
    print(f"Az óra végen {osszegzes} lett a pénztárcájá-ban")
    if elso != -1:
        print(f"Az első tíz fontnál többet fizető vendég a, {elso + 1}  volt.")
        print(f"Az utolsó tíz fontnál többet fizető vendég a, {utolso + 1} volt.")
    


# Fő program

# 1 input
osszegek = beolvasas()

# 2 Számítás
osszegzes = szamitas(osszegek)
elso, utolso = eldontes(osszegek)

# 3 output
kiir(elso, utolso,osszegzes)
