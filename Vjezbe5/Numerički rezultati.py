import calculus as calc
print(calc.funkcija("sin(x)", 0))
print(calc.derivacija_u_tocki_twostep("sin(x)", 0))
print(calc.derivacija_u_tocki("sin(x)", 0))
calc.integracija_numericki("sin(x)", 0, 4, 10000)
print(calc.integracija_trapezna("sin(x)", 0, 4, 10000))

print(calc.funkcija("x**3", 0))
print(calc.derivacija_u_tocki_twostep("x**3", 0))
print(calc.derivacija_u_tocki("x**3", 0))
calc.integracija_numericki("x**3", 0, 4, 10000)
print(calc.integracija_trapezna("x**3", 0, 4, 10000))

