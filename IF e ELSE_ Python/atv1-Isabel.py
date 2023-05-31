num = int(input("Insira o número a ser validado: "))

if(num > 0):
    print(input("O valor", num, "é positivo."))
elif(num == 0):
    print("O valor", num, "é neutro.")
else:
    print("O valor", num, "é negativo.")