"""
szam=int(input("kerek egy egesz szamot") )
szam1=int(szam)
if szam>0:
       print("a szam pozitiv")
elif szam1==0:
        print("a szam nulla")
else:
            print("a szam negativ")

x=int(input("kerek egy szamot"))
y=int(input("kerek egy szamot"))

if x>0 and y>0: 
    print("elso negyed")

elif x>0 and y<0:
    print("masodik negyed")

elif x<0 and y<0:
    print("harmadik negyed")

elif x>0 and y>0:
    print("negyedik negyed")

elif x=0 and y=0:
    print("origo")
"""

"""#paros szam-e?
c=int(input("kerek egy egesz szamot"))
if c%2==0:
    print("paros szam")

else :
    print("paratlan szam")  """
"""
n=int(input("kerek egy szamot"))
m=int(input("kerek egy masik szamot"))
if m!=0:
        if n%m==0:
            print("n oszthato m-el")
        else:
            print("n nem oszthato m-el")

else: 
        print("0 nem adhato meg")

"""
"""
a=int(input("kerek egy A-t"))
b=int(input("kerek egy B-t"))
n=int(input("kerek egy N-t"))

if n>a and n<b:
    print(",n, A és B között van")

elif n<a and n>b:
            print(",n, A és B között van")

elif n<a and n<b:
            print(",n, nem A és B között van")

elif n>a and n>b:
            print(",n, nem A és B között van") """

jegy=int(input("kerek egy szamot"))

if jegy==1:
    print("elégtelen")

elif jegy==2:
    print("elégséges")

elif jegy==3:
    print("közepes")

elif jegy==4:
    print("jó")

elif jegy==5:
    print("jeles")

else:
    print("nincs ilyen")