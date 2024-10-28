eggs = int(input("Number of eggs: "))

doz = eggs//12

rem = eggs%12

calc = 0

if 0 < doz <= 4:
    calc = .50
elif doz > 4 and doz <= 6:
    calc = .45
elif doz > 6 and doz <= 11:
    calc = .40
elif doz > 11:
    calc = .35

print("The bill is equal to: $"+str((doz*calc)+(rem*(calc*(1/12)))))


input()
