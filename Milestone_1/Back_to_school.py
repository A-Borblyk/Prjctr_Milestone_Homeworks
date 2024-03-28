eq = "5x^2 + (-5)x + (-10) = 0"
eq = eq.replace(" ", "").replace("(", "").replace(")", "").replace("=0", "")
eq = eq.replace("x^2+", " ").replace("x+", " ")
eq = eq.split()

a = int(eq[0])
b = int(eq[1])
c = int(eq[2])

print(a, b, c)

discrim = (b**2 - 4*a*c)**0.5
x1 = (-b + discrim) / (2 * a)
x2 = (-b - discrim) / (2 * a)
print(x1, x2)
