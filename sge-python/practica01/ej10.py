# Escribe un programa que calcule potencias para un número dado. El programa debe pedir un número y a continuación
# calcular el cuadrado, el cubo, la potencia cuarta y la potencia quinta. En python se puede calcular el cubo de un
# número de dos formas:

numero = int(input("Dame un número: "))
for i in range(2, 6):
    print(f"{numero} ^ {i} = {numero ** i}")
