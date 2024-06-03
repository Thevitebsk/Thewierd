a = 0
global command
command = 1
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
    a=int(input("ENTER YOUR NUMBER HERE:"))
while True:
    i = input(">>")
    if "+" in i:
        ad()
    if "-" in i:
        m()
    if "'" in i:
        q()
    if "№" in i:
        num()
    if a >= 128:
        a = 0
    command += 1
