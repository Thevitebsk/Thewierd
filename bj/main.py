a=" ABCDEFGHIJKLMNOPQRSTUVWXYZ";b=m=0
while 1:
 m=b=0
 for c in input("\n>"):
  if c=="+":b+=1
  elif c=="-":b-=1
  elif c=="'":print(end=a[b])
  elif c=="`":b=int(input("num:"))
  elif c=="^":m=b;b=0
  elif c=="v":b=m;m=0
  b=b%26
  if b<0:b=25
