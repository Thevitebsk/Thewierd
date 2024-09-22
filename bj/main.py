a=" ABCDEFGHIJKLMNOPQRSTUVWXYZ";c=0;s=0
while True:
 s=0;c=0
 for c in input("\n>"):
  if c=="+":c+=1
  elif c=="-":c-=1
  elif c=="'":print(a[c], end='')
  elif c=="`":c=int(input("CSVAL:"))
  elif c=="^":s=c;c=0
  elif c=="v":c=s;s=0
  elif c=="#":break
  if c<0 or c>25:c=0
