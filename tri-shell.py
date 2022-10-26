# Tri Shell
# English: Shell Sort

def tri_shell(tab, n):
  # Calculer the plus grand pas qui est supérieur à n
  pas = 0
  while pas < n:
    pas = pas * 3 + 1

  while pas > 0:
    pas = pas // 3
    for i in range(pas, n):
      aux = tab[i]
      j = i - pas
      while j > -1 and tab[j] > aux:
        tab[j + pas] = tab[j]
        j = j - pas
      tab[j + pas] = aux
  return tab

tab = [13, 0, 8, 1, 22, 3, 1, 2, 5]
n =  len(tab)
print(tri_shell(tab, n))