import time
import random



def DeretAjaib_iteratif(n):
    myDeret = [1,2,3,4,5]

    for i in range(n):
        pointA = (len(myDeret)+1) - 2
        pointB = (len(myDeret)+1) // 2
        angkaAjaib = myDeret[pointA-1] + myDeret[pointB-1]
        myDeret.append(angkaAjaib)
    

start = time.time()
for i in range(6,101):
    DeretAjaib_iteratif(i)
    end = time.time()
    print('Suku ke-',i, '= ', (end-start))


##############################################################

def DeretAjaib_rekursif():
    myDeret = [1,2,3,4,5]

    pointA = (len(myDeret)+1) - 2
    pointB = (len(myDeret)+1) // 2
    angkaAjaib = myDeret[pointA-1] + myDeret[pointB-1]
    myDeret.append(angkaAjaib)
    
    if len(myDeret) == 100:
        return True
    else:
        return 

start = time.time()
for i in range(6,101):
    DeretAjaib_rekursif()
    end = time.time()
    print('Suku ke-',i, '= ', (end-start))