a = 0
e=[]
def ad():
    global a
    a += 1
def m():
    global a
    a -= 1
def q():
    print(a)
def num():
    global a
    a=int(input("number:"))
while True:
    i = input(">>")
    for char in i:
        if char == "+" and "+" not in e:
            ad()
        if char == "-" and "-" not in e:
            m()
        if char == "'" and "'" not in e:
            q()
        if char == "№" and "№" not in e:
            num()
        if a >= 27:
            a = 0
        continue
