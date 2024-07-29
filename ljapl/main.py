print("""
L       J    A    PPPP L
L       J   A A   P  P L
L       J  AAAAA  PPPP L
LLLL JJJ  A     A P    LLLL
""")
n="\n"
while True:
  nc=0
  se=f"0123456789{n} abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]`|~"
  s=[]
  store=[]
  out=[]
  for c in input():
    nc+=1
    if c == "+":
      r=int(s[0])+int(s[1])
      s.append(r)
      s.pop(0)
      s.pop(0)
    elif c == "0":
      s.append(0)
    elif c == "1":
      s.append(1)
    elif c == "2":
      s.append(2)
    elif c == "3":
      s.append(3)
    elif c == "4":
      s.append(4)
    elif c == "5":
      s.append(5)
    elif c == "6":
      s.append(6)
    elif c == "7":
      s.append(7)
    elif c == "8":
      s.append(8)
    elif c == "9":
      s.append(9)
    elif c == "a":
      s.append(10)
    elif c == "b":
      s.append(11)
    elif c == "c":
      s.append(12)
    elif c == "d":
      s.append(13)
    elif c == "e":
      s.append(14)
    elif c == "f":
      s.append(15)
    elif c == "g":
      s.append(16)
    elif c == "C":
      out.append(se[int(s[0])])
      s.pop(0)
    elif c == "N":
      out.append(int(s[0]))
      s.pop(0)
    elif c == "S":
      out.append(s[0])
      s.pop(0)
    elif c == "|":
      print("output:")
      print(out[0])
      break
    elif c == "&":
      r=str(s[0])+str(s[1])
      s.append(r)
      s.pop(0)
      s.pop(0)
    elif c == "?":
      print(s)
    elif c == "*":
      r=int(s[0])*int(s[1])
      s.append(r)
      s.pop(0)
      s.pop(0)
    elif c == "/":
      r=int(s[0])/int(s[1])
      s.append(r)
      s.pop(0)
      s.pop(0)
    elif c == ":":
      s.append(s[0])
    elif c == "-":
      r=int(s[0])-int(s[1])
      s.append(r)
      s.pop(0)
      s.pop(0)
    elif c == "%":
      r=int(s[0])%int(s[1])
      s.append(r)
      s.pop(0)
      s.pop(0)
    elif c == ";":
      s.append(s[0])
      s.pop(0)
    elif c == "_":
      inp=input("input:\n")
      s.append(inp)
    elif c == "^":
      if len(s) == 0:
        print(f"x{n}EMPTY STACK{n}EDIT COMMAND {nc}")
      else:
        store.append(int(s[0]))
        s.pop(0)
    elif c == "v":
      s.append(int(store[0]))
      store.pop(0)
    elif c == "[":
      if s[0]==s[1]:
        s.append(1)
        s.pop(0)
        s.pop(0)
      else:
        s.append(0)
        s.pop(0)
        s.pop(0)
    elif c == "]":
      if s[0]!=s[1]:
        s.append(1)
        s.pop(0)
        s.pop(0)
      else:
        s.append(0)
        s.pop(0)
        s.pop(0)
    elif c == "r":
      b=str(s[0]).replace(str(s[1]), "")
      s.append(b)
      s.pop(0)
      s.pop(0)
    elif c == "~":
      print(s)
    else:
      print(f"x{n}UNKNOWN COMMAND{n}EDIT COMMAND {nc}")
      break
    if len(out) == 2:
      r=str(out[0])+str(out[1])
      out.append(r)
      out.pop(0)
      out.pop(0)
