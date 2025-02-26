T=int(input(""))
x=[]
d=[]
for i in range(1,T+1):
    x1,y1,r1,x2,y2,r2=map(int, input("").split())
    d.append(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    x.append([x1,y1,r1,x2,y2,r2])
for j in range(len(x)):
  if d[j] == 0 and x[j][2] == x[j][5]:
    print(-1)

  elif x[j][2] + x[j][5] == d[j] or abs(x[j][2] - x[j][5]) == d[j]:
    print(1)

  elif abs(x[j][2] - x[j][5]) < d[j] < x[j][2] + x[j][5]:
    print(2)

  else:
    print(0)
    