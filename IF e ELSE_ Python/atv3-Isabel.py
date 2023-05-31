salario = int(input("Insira o valor do salário deste mês: "))
internet = int(input("Insira o valor da despesa com Internet deste mês: "))
agua = int(input("Insira o valor da despesa com Água deste mês: "))
energia = int(input("Insira o valor da despesa com Energia deste mês: "))

total = (internet+agua+energia)
print("O valor do salario é: ", salario, "E o total das despesas", total)

if(total >= salario):
    print("Orçamento estourado!")
else:
    print("Gastos dentro do orçamento!")

