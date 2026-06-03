X = float(input("Введите минимальную сумму инвестиций (X): "))
A = float(input("Сколько долларов у Майкла (A): "))
B = float(input("Сколько долларов у Ивана (B): "))

mike_can = A >= X      # Майкл один
ivan_can = B >= X      # Иван один
together_can = (A + B) >= X   # вместе

if mike_can and ivan_can:
    print(2)
elif mike_can and not ivan_can:
    print("Mike")
elif not mike_can and ivan_can:
    print("Ivan")
elif together_can:
    print(1)
else:
    print(0)
