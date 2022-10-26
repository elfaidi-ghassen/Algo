
def tri(tab, n):
  for i in range(n//2):
    pos_min = i
    #! Si vous utilisez (pos_max = i), il ne marche pas!
    pos_max = n - i - 1
    for j in range(i + 1, n - i):
      if tab[j] < tab[pos_min]:
        pos_min = j
      if tab[j] > tab[pos_max]:
        pos_max = j
    if i != pos_min:
      aux = tab[pos_min]
      tab[pos_min] = tab[i]
      tab[i] = aux

    if i != pos_max:
      aux = tab[pos_max]
      tab[pos_max] = tab[n - i - 1]
      tab[n - i - 1] = aux
  return tab


tab = [13, 0, 8, 1, 22, 3, 1, 2, 5]
n =  len(tab)
print(tri(tab, n))