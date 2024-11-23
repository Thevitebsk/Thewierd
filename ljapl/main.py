print("""
L       J    A    PPPP L
L       J   A A   P  P L
L       J  AAAAA  PPPP L
LLLL JJJ  A     A P    LLLL""")
n="\n"
while True:
  se=f"0123456789{n} abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]`|~"
  s=[];nc=0;b=[];e=0
  out=[]
  for c in input("code:\n"):
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
    elif c == "C":
      out.append(se[int(s[0])])
      s.pop(0)
    elif c == "N":
      out.append(int(s[0]))
      s.pop(0)
    elif c == "|":print("output:",out[0:]sep="\n");break
    elif c == "&":
      r=str(s[0])+str(s[1])
      s.append(r)
      s.pop(0)
      s.pop(0)
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
    elif c == "=":
      s.append(s[0])
    elif c == "-":
      r=int(s[0])-int(s[1])
      s.append(r)
      s.pop(0)
      s.pop(0)
    elif c == ";":
      s.append(s[0])
      s.pop(0)
    elif c == "_":
      inp=input("input:\n")
      s.append(inp)
    else:
      print(f"x{n}UNKNOWN COMMAND{n}EDIT COMMAND {nc}")
      break
  if c=="e":break
