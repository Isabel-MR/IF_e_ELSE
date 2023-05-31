salario = int(input("Insira o valor do seu salário:"))

if (salario < 500):
    novo_salario = salario * 0.15
elif (salario <= 1000):
    novo_salario = salario * 0.10
elif(salario > 1000):
    novo_salario = salario * 0.05

print("O seu novo salário é: ", novo_salario)


