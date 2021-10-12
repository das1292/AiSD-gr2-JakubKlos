def foo(a):
    dni = ["poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela"]
    a==oct(a)
    if a>=1 and a<8:
        return dni[a-1]
    else:
        return print("Podaj liczbę od 1 do 7")
print(foo(8))
