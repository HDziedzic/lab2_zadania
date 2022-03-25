import sys as system
# zad 1
from math import sqrt

print("-----------------zadanie 1----------------")

lista_sporty = ['łucznictwo', 'lekkoatletyka', 'noks', 'szachy', 'kajakarstwo', 'wspinaczka', 'golf']
lista_sporty.reverse()
lista_sporty.extend(('rzut dyskiem', 'skok w dal', 'rugby', 'gimnastyka'))
print(lista_sporty)

# zad 2
print("-----------------zadanie 2----------------")

skroty = {"wg": "według",
          "itp.": "i tym podobne",
          "s.": "strona",
          "p.o.": "pełniacy obowiązki",
          "itd.": "i tak dalej",
          "pw.": " pod wezwaniem"
          }
print(skroty)
# zad 3
print("-----------------zadanie 3----------------")

gry_slownik = {"FPS": "Overwatch",
               "RPG": "Wiedźmin 3: Dziki Gon",
               "zręcznościowa": "Cuphead",
               "Przygodowa": "Life is Strange",
               "Battle Royale": "Call of Duty: Warzone",
               "symulator": "My Samer Car"}
print(len(gry_slownik))

# zad 4
print("-----------------zadanie 4----------------")

zdanie = input("Wprowadź zdanie:\n ")
ile_a = 0
for i in range((len(zdanie))):
    if zdanie[i] == 'a':
        ile_a += 1
print(ile_a)

# zadanie 5
print("-----------------zadanie 5 ----------------")

system.stdout.write("podaj liczbę a: ")
a = system.stdin.readline()
system.stdout.write("podaj liczbę b: ")
b = system.stdin.readline()
system.stdout.write("podaj liczbę c: ")
c = system.stdin.readline()

wynik = int(a) ** int(b) + int(c)
print(wynik)

# zad 6
print("-----------------zadanie 6----------------")
a = input("podaj a:\n")
b = input("podaj b:\n")
c = input("podaj c:\n")

tab = [int(a), int(b), int(c)]
print("największą liczbą jest: ", max(tab))

# zad 7
print("-----------------zadanie 7----------------")

lista = [2, 2.6, 5, 2.1, 3.14, 6, 12]

for i in range(len(lista)):
    lista[i] = lista[i] ** 2
print(lista)

# zad 8
print("-----------------zadanie 8----------------")

lista_zad8 = []
i = 0
while i < 10:
    a = input("podaj liczbe: ")
    if int(a) % 2 == 0:
        lista_zad8.append(a)
    i += 1
print(lista_zad8)

# zad 9
print("-----------------zadanie 9----------------")

n = input("Podaj liczbę:\n")
x = int(n)
if x >= 0:
    print("pierwiastek z {liczba} = {liczbaa}".format(liczba=x, liczbaa=sqrt(x)))
else:
    print("liczba ujemna...")
