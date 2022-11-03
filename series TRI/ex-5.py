from pickle import *
from numpy import *

def remplir(fb):
  n = 0
  x = int(input("donner un entier: "))
  while x != -1:
    dump(x, fb)
    x = int(input("donner un entier: "))
    n += 1
  return n

def tri(fb, n, ft):
  for i in range(n):
    x = load(fb, allow_pickle=True)
    t[i] = x
  for i in range(n):
    pos_min = i
    for j in range(i + 1, n):
      if t[pos_min] > t[j]:
        pos_min = j
    if pos_min != t[i]:
      aux = t[i]
      t[i] = t[pos_min]
      t[pos_min] = aux

  ch = ""
  s = 0
  for i in range(n):
    ch = ch + "," + str(t[i])
    s = s + t[i]
  ft.write(ch[1:] + "\n")
  ft.write("somme = " + str(s) + "  " + "moyenne = " + str(s / n))

# PP
fb = open("f.dat", "wb")
n = remplir(fb)
fb.close()
t = array([0] * n)

ft = open("f.txt", "w")
fb = open("f.dat", "rb")
tri(fb, n, ft)
ft.close()
fb.close()
