a=" ABCDEFGHIJKLMNOPQRSTUVWXYZ";ac=0;m=0
while True:
 s=0;ac=0
 for c in input("\n>"):
  if c=="+":ac+=1
  elif c=="-":ac-=1
  elif c=="'":print(end=a[ac])
  elif c=="`":ac=int(input("num:"))
  elif c=="^":m=ac;ac=0
  elif c=="v":ac=m;m=0
  elif c=="#":ac=0
  if ac<0:ac=25
  elif ac>25:ac=0
