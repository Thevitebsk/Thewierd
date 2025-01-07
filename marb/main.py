import sys,time
y=x=mv=0;st=[];arg=sys.argv[1:];debug=0;s=1;out="";dd=1
while arg:
 if arg[0]=="-d":debug=1
if debug:dd=16
c="""
_
"""
a=c[1:-1].split("\n")
while 1:
 if debug==1:print(f"STEP {s}",f"{a[y][x]} {y} {x} {mv}","==================="*2,sep="\n")
 if a[y][x]=="\\":x+=1;y-=1
 elif a[y][x]=="/":x-=1;y-=1
 elif a[y][x]=="_":print(out);break
 elif a[y][x]=="=":y=0-1
 elif a[y][x]=="[":st.append(mv)
 elif a[y][x]=="+":mv+=1
 elif a[y][x]=="-":mv-=1
 elif a[y][x]=="^":
  if st.pop():x+=1;y-=1
  else:x-=1;y-=1
 elif a[y][x]=="?":st.append(int(input()))
 elif a[y][x]==".":out+=str(st.pop())
 if s==4096//dd:print(out);break
 y+=1;s+=1
 if y>len(a)-1:print("Your marble has escaped");break
