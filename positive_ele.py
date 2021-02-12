lst = []
n= int (input ("Enter no. of elements :"))

for i in range (0,n):
    e= int (input ())
    if e>0:
        lst.append(e)

print ("List :")
for i in range(0, len(lst)):
    print(lst[i], end=" ")
    
