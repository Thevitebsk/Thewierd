at="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ocm = 0
osm = ""
while True:
 for c in input("\n>"):
  if c == "+":
   ocm += 1
  elif c == "-":
   ocm -= 1
  elif c == "'":
   print(at[ocm], end='')
  elif c == "`":
   ocm = int(input("CSVAL:"))
  elif c == "^":
   osm=ocm
   ocm=0
  elif c == "v":
   if osm=="":
    print("X")
    break
   ocm=osm
   osm=""
  elif c == "r":
   osm=0
   ocm=0
  elif ocm < 0 or ocm > 25:
   ocm = 0
  else:
   print("X")
   break
