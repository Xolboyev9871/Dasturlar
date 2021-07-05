'''1-misolA={1, 2, 3, 4, 5, 7, 9,"olma"}
print(A)


2-misolA={1, 2, 3, 4, 5, 7, 9,"olma"}
A.add(10)
print(A)

3-misola={1, 2, 3, 4, 5, 7, 9,"olma"}
a.remove(1)
a.discard(3)
print(a)

4-misol:
a={1, 2, 3, 4, 5, 7, 10,}
b={1, 6, 1, 4, 12, 7, 10,}
a.intersection_update(b)
print(a)

5-misol:
a={1, 2, 3, 4, 5, 7, 10,}
b={1, 6, 1, 4, 12, 7, 10,}

print(a|b)

#6-misol
a={1, 2, 3, 4, 5, 7, 10,}
b={1, 6, 3, 4, 12, 7, 10,}

print(b-a)


#7-misol
a={1, 2, 3, 4, 5, 7, 10,}
b={1, 6, 3, 4, 12, 7, 10,}
print(a.symmetric_difference(b))


#8-misol
a={1, 2, 3, 4, 5, 7, 10, 11, 15, 20}
b={1, 2, 3, 4, 5, 7, 10}
print(a.issuperset(b))

#9-misol
a={1, 2, 3, 4, 5, 7, 10, 11, 15, 20}
b={1, 2, 3, 4, 5, 7, 10}
a.clear()
print(a)


#10-misol
A=frozenset([1, 2, 3])
print(type(A))

#11-misol
a={1, 2, 3, 4, 5, 7, 10, 11, 15, 20}
print(len(a))

#12-misol
a={1, 2, 3, 4, 5, 7, 10, 11, 15, 20}
print(4 in a)

#13-misol
a={1, 2, 3, 4, }
b={5, 7, 10,}
print(a.isdisjoint(b))


#Narda o'yinini oynash
from random import randint
run=True
while run:
    z1=randint(1, 7)
    z2=randint(1, 7)
    print("1-tosh", z1)
    print("2-tosh", z2)
    print("Yana o'ynaysizmi? ha-1, yo'q-0")
    run=int(input())
else:
    print("O'yin uchun raxmat")'''

print("Yil nomoni kiriting!")
y=int(input())
if y%4==0:
    if y%400==0:
        print("Kabisa yili")
    else:
        print("Kabisa yili emas")
        




    
