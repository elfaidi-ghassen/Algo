from numpy import *

def freq(tab, x):
  a = 0
  for i in range(n):
    if len(tab[i]) == len(x):
      a = a + 1
  return a

def tri(t, n):
  pas = 0
  while pas < n:
    pas = pas * 3 + 1

  while pas > 0:
    pas = pas // 3
    for i in range(pas, n):
      j = i - pas
      x = t[i]
      while j > -1 and len(t[j]) < len(x):
        t[j + pas] = t[j]
        j = j - pas
      t[j + pas] = x

  ft = open("f.txt", "w")
  done = []
  for i in range(n):
    freqs = freq(t, t[i])
    if (len(t[i]) not in done):
      ft.write("longeur = " + str(len(t[i])) + ": " + "il y'a " + str(freqs) + " mots\n")
      done.append(len(t[i]))
  ft.close()



# PP
t = array(["abc", "reddof", "def", "kao", "mr", "lemme", "canon"])
n = 7
tri(t, n)
print(t)