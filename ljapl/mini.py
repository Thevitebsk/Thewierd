#this is a temporary file. it will be moved to main.py after it's finished
print("""
L       J    A    PPPP L
L       J   A A   P  P L
L       J  AAAAA  PPPP L
LLLL JJJ  A     A P    LLLL""")
n="\n"
while True:
  ce=f"0123456789{n} abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]`|~"
  s=[];nc=0;b=[];e=0;num=[]
  out=[];inp=input("code:")
  for _ in range(10):num.append(str(_))
  if inp[nc]=="+":s.append(int(s.pop(0))+int(s.pop(0)))
