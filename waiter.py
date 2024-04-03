def beolvasas():
    adatok=[]
    with open("adatok.txt","r",encoding="UTF-8")as fm:
        for sor in fm:
            adatok.append(float(sor.strip()))
    return adatok

osszegek=beolvasas()

print(osszegek)

def szamitas(a):
    return sum(a)
     
asd=szamitas(osszegek)
print(asd)



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

elso,utolso = eldontes(osszegek)

if elso != -1:
    print("Az első tíz fontnál többet fizető vendég a", elso + 1, ". volt.")
    print("Az utolsó tíz fontnál többet fizető vendég a", utolso + 1, ". volt.")
else:
    print("Nem volt olyan vendég, aki tíz fontnál többet fizetett.")
