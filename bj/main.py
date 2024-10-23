a=" ABCDEFGHIJKLMNOPQRSTUVWXYZ";b=0;m=0
while True:
 m=0;b=0
 for c in input("\n>"):
  if c=="+":b+=1
  elif c=="-":b-=1
  elif c=="'":print(end=a[b])
  elif c=="`":b=int(input("num:"))
  elif c=="^":m=b;b=0
  elif c=="v":b=m;m=0
  elif c=="#":b=0
  if b<0:b=25
  elif b>25:b=0
