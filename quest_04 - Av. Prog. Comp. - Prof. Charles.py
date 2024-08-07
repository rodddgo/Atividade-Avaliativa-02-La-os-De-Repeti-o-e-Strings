#lista dos n validos
num_validos = list()

for num in range(2, 1000000):
    if num % 2 == 0 or num % 5 == 0:   #se n for mult de 2 ou mult de 5
        
        #soma dig
        soma = 0
        numstr = str(num)
        for i in numstr:
            soma += int(i)**5

        #adicionando os num na lista de valores
        if soma == num: num_validos.append(num)
        
print(num_validos)