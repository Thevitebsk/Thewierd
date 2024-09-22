a=" ABCDEFGHIJKLMNOPQRSTUVWXYZ";ocm=0;osm=""
while True:
 s="";c=0
 for c in input("\n>"):
  if c == "+":c+=1
  elif c == "-":c-=1
  elif c == "'":print(a[c], end='')
  elif c == "`":c=int(input("CSVAL:"))
  elif c == "^":s=c;c=0
  elif c == "v":c=s;s=""
  else:print("X");break
  if c<0 or c>25:c=0
