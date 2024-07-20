#+ - adds to the 1 cell memory
#- - subtracts from the 1 cell memory
#' - prints the 1 cell memory value as the "at" charecter
#` - Gets user input and sets the 1 cell memoery to that value
#^ - Pushes the value to the one stack memory
#v - Sets the one memory cell to the value from the one stack memory
#examples
#+++++++'^++++'v++++''+++'++++++++'--------'+++'^+++++++++++'--------' - Hello World
at="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ocm = 0
osm = 0
e=[]
def a():
    global ocm
    ocm += 1
def m():
    global ocm
    ocm -= 1
def q():
    global ocm
    print(at[ocm], end='')
def iq():
    global ocm
    ocm = int(input("CSVAL:"))
def x():
    global osm
    global ocm
    osm=ocm
    ocm=0
def ix():
    global osm
    global ocm
    ocm=osm
    osm=0
def r():
        global osm
        global ocm
        osm=0
        ocm=0
while True:
    i = input(">")
    for c in i:
        if c == "+" and "+" not in e:
            a()
        if c == "-" and "-" not in e:
            m()
        if c == "'" and "'" not in e:
            q()
        if c == "`" and "`" not in e:
            iq()
        if c == "^" and "^" not in e:
            x()
        if c == "v" and "v" not in e:
            ix()
        if c == "r" and "r" not in e:
            r()
        if ocm < 0 or ocm > 25:
            ocm = 0
    print("\n")
    continue
