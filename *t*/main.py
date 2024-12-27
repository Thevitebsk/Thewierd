num=list(map(str,range(10)));stack=[]
out="";code="""

"""
s=0;tr=0;p=0;code=code[1:len(code)-1]
if code=="":s=1;out+=input()
while len(code)>p and s==0:
 if len(out)>1023:tr=1;break
 if code[p]in num:stack.append(int(num[int(code[p])]))
 p+=1
if tr:print("T")
print("~"*15+" RESULT "+"~"*15)
print(out,"~"*38,"STACK: "+str(stack),sep="\n")
