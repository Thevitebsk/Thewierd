#+ - adds to the 1 cell memory
#- - subtracts from the 1 cell memory
#' - prints the 1 cell memoery value
#` - Gets user input and sets the 1 cell memoery to that value
#^ - Pushes the value to the one stack memory
#v - Sets the one memory cell to the value from the one stack memory
#examples
#++++++++'^+++++'v++++''+++'^'+++++++++++++++++++++++'v'+++'------'--------' - Hello World
loat=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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
    print(loat[ocm], end='')
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
while True:
    i = input(">>")
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
    print("\n")
    if a > 26:
        a = 0
    continue
