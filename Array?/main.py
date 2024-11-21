print("Array?")
c="""□""";p=0;m=0;s=[];ar=[];i=input();i=i.split()
while p<len(c):
 if c[p]=="[" and m==0:m=1
 elif m==1:
  if c[p]=="," and c[p-1]!="\\":
   while len(s)>1:a=str(s[0])+str(s[1]);s.pop(0);s.pop(0);s.reverse();s.append(a);s.reverse()
   ar.append(s[0]);s.pop(0)
  s.append(c[p])
  if c[p]=="]":
   m=0;s.pop()
   if s[0]==",":
    s.pop(0)
   while len(s)>1:a=str(s[0])+str(s[1]);s.pop(0);s.pop(0);s.reverse();s.append(a);s.reverse()
   ar.append(s[0].replace("\\",""));s.pop(0)
 elif c[p]=="∃":
  while c[p]!="∄":p+=1
 elif c[p]=="□":ar.append(i.pop(0))
 p+=1
while len(ar)>0:print(ar[0]);ar.pop(0)
