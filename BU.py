at=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = 0
e=[]
def ad():
    global a
    a += 1
def m():
    global a
    a -= 1
def q():
    global a
    a = at[5]
    print(a)
def dq():
    global a
    a = input
    
while True:
    i = input(">>")
    for c in i:
        if c == "+" and "+" not in e:
            ad()
        if c == "-" and "-" not in e:
            m()
        if c == "'" and "'" not in e:
            q()
        if c == "`" and "`" not in e:
            dq()
        if a >= "Z":
            a = 0
        continue
