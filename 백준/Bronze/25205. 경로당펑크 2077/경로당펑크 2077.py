N=int(input())
A=input()
last=ord(A[-1])
if last==114 or last==115 or last==101 or last==102 or last==97 or last==113 or last==116 or last==100 or last==119 or last==99 or last==122 or last==120 or last==118 or last==103:
    print(1)
else:
    print(0)