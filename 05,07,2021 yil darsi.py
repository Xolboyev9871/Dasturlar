royxat={
    'white':"oq",
    'black': "qora",
    'blue': "ko'k",
    'yellow': "sariq",
    'green': "yashil",
    'red':"qizil",
    'brown':"jigarrang",
    'purple': "suyohrang",
    'filoet': "binafsha",
    'orange': "olovrang"
    }
for i, j in royxat.items():
        print(i, "-", j)

run =True
while run:
    rang=input("Ingilizcha ranglar nomini kiriting? [x-exit] :")
    if rang=='x':
        break
    if rang in royxat: 
        print(royxat[rang])
    else:
        print("Bunday rang yoq. Bizda bor ranglar")
        for i in royxat:
            print(i, end=" * ")
print("Dastur tugadi")




    
    

