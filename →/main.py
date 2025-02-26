print("→\na brother to branjunk")
while 1:
    p=0;m=[];i=input("\n>>")
    while 1:
        if i[p]=="+": m.append(m.pop()+m.pop())
        elif i[p]=="-": m.append(m.pop()-m.pop())
        elif i[p]=="*": m.append(m.pop()*m.pop())
        elif i[p]=="/": break
        elif i[p]in list(map(str,range(10))): m.append(int(i[p]))
        elif i[p]=="?": m.append(int(input()))
        elif i[p]=="`": print(m.pop())
        elif i[p]=="#": 
            if m.pop():...
            else:p+=1
        if p>=len(i)-1:p=-1
        p+=1
