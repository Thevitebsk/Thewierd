import sys;y=x=mv=wy=c=0
st=[];out=""
code="""
_
"""
a=code[1:-1].split("\n")
while 1:
 try:
  if a[y][x]=="\\":x+=1;y-=1
  elif a[y][x]=="/":x-=1;y-=1
  elif a[y][x]=="_":print(out);break
  elif a[y][x]=="=":
    wy=y;y=0
    while y<len(a):
     try:
      if a[y][x]=="_":y=wy;c=1;break
      else:y+=2
     except IndexError:y+=2
    if not c:y=0
    y+=1
  elif a[y][x]=="[":st.append(mv)
  elif a[y][x]=="+":mv+=1
  elif a[y][x]=="-":mv-=1
  elif a[y][x]=="^":
   if st.pop():x+=1;y-=1
   else:x-=1;y-=1
  elif a[y][x]=="?":st.append(int(input()))
  elif a[y][x]==".":out+=str(st.pop())
  if len(out)==4096*4:print(out);break
  y+=1
  if y>len(a)-1:print("Your marble has escaped");break
 except IndexError:continue
