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