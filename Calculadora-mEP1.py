x = float(input())
op = (input())
y = float(input())
#(“+”, “-”, “*”, “//”, “%”, “**”) operações admitidas
if op == "+":
    print(f"{x} + {y} = {x+y}")
elif op == "-":
    print(f"{x} - {y} = {x-y}")
elif op == "*":
    print(f"{x} * {y} = {x*y}")
elif op == "//":
    print(f"{x} // {y} = {x//y}")
elif op == "%":
    print(f"{x} % {y} = {x%y}")
elif op == "**":
    print(f"{x} ** {y} = {x**y}")
else:
    print("Operacao nao reconhecida!")
#falta a parte de divisão por 0
