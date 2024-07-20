#X++++++++'++++^+++++'v''+++'^'v++++++++'--------'+++'------'--------' - Hello World
at=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ocm = ""
osm = ""
while True:
 osm=""
 ocm=""
 for c in input("\n>"):
  if c == "+":
   if ocm=="":
    print("X")
    break
   ocm += 1
  elif c == "-":
   if ocm=="":
    print("X")
    break
   ocm -= 1
  elif c == "'":
   if osm=="":
    print("X")
    break
   print(at[ocm], end='')
  elif c == "`":
   ocm = int(input("CSVAL:"))
  elif c == "^":
   if ocm=="":
    print("X")
    break
   osm=ocm
   ocm=0
  elif c == "v":
   if osm=="":
    print("X")
    break
   ocm=osm
   osm=""
  elif c == "X":
   ocm=0
  else:
   print("X")
   break
  if ocm < 0 or ocm > 25:
   ocm = 0
