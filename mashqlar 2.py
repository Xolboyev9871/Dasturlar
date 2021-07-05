'''1-misol. from random import *
list=[]
for i in range(10):
      list.append(randint(20, 50))
print(list)

mevalar=["olma","gilos", "yongoq", "olhori", "banan"]
s=len(mevalar)
meva=input()
for i in range(0,s):
      if mevalar[i]==meva:
            print("bor")
            continue
      else:
            print("yo'q")
            continue

mevalar = ["banan", "olma", "nok", "gilos","anor"]

for i in range(len(mevalar)):
  mevalar[i] = mevalar[i].upper()

print(mevalar)

meva = input("Meva kirit: ").upper()
print(meva)

if meva in mevalar:
  print("Bunday meva bor")
else:
  print("Bunday meva yoq")

s=[1,4,6,7,8,4]
j=[]
t=[]
for i in s:
      if i%2==0:
            j.append(i)
            
      else:
            t.append(i)
print(t)
print(j)'''

R=["Ali","Vali","Soli"]
R.sort()
R.reverse()
print(R)
  
      
