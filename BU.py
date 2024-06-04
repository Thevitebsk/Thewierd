ASCIITABLE = {
    ' ':0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
    'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
    'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
    'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
    'Y': 25, 'Z': 26
}
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
