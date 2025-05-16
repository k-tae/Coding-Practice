ISBN=input()
a=0
for i in range(13):
    if ISBN[i]=='*':
        k=i
        pass
    elif i%2==0:
        a+=int(ISBN[i])
    else:
        a+=3*int(ISBN[i])
D=a%10
if k%2==0:
    print(10-D)
else:
    if D==1:
        print(3)
    elif D==2:
        print(6)
    elif D==3:
        print(9)
    elif D==4:
        print(2)
    elif D==5:
        print(5)
    elif D==6:
        print(8)
    elif D==7:
        print(1)
    elif D==8:
        print(4)
    elif D==9:
        print(7)
    elif D==0:
        print(0)