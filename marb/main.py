import sys,time
y=x=mv=0;st=[];arg=sys.argv[1:];debug=1;s=1
while arg:
 if arg[0]=="-d":debug=1
c="""
_
"""
a=c[1:-1].split("\n")
while 1:
 if debug==1:print(f"STEP {s}",f"{a[y][x]} {y} {x} {mv}","==================="*2,sep="\n");s+=1;time.sleep(0.5)
 if a[y][x]=="\\":x+=1;y-=1
 elif a[y][x]=="/":x-=1;y+=1
 elif a[y][x]=="_":print("".join(s));break
 elif a[y][x]=="=":y=0-1
 elif a[y][x]=="[":st.append(mv)
 elif a[y][x]=="+":mv+=1
 elif a[y][x]=="-":mv-=1
 y+=1
 if y>len(a)-1:print("Your marble has escaped");break "+str(stack),"VARIABLES: "+str(var),sep="\n")
if tr==1:print("TRUNCATED")
