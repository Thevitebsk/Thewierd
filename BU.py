a = 0
command = 1
i = input(">>")[command]
def ad():
    global a
    a += 1
def m():
    global a
    a -= 1
def q():
    print(a)
while True:
    if "+" in i:
        ad()
    if "-" in i:
        m()
    if "'" in i:
        q()
    if a >= 128:
        a = 0
