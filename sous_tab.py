def sous_tab(tab, e, f):
    sous_tab = []
    c = 0
    for i in range(e, f):
        c += 1

    for i in range(e, f):
        sous_tab.append(tab[i])
    return sous_tab


t = []
for i in range(0, 10):
    t.append(int(input(f"donner l'element {i+1} : ")))


e = int(input("entrer un entier de debut : "))
f = int(input("entrer un entier de fin : "))
if f< e:
    c = e
    e = f
    f = c
resultat = sous_tab(t, e, f)
print(resultat)
