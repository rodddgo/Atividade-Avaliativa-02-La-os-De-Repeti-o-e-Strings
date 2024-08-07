import sys

num = int(input('Insira um número inteiro positivo: '))

#verificando se num positivo
if num <= 0:
    sys.exit("Erro! O número deve ser um inteiro positivo!!")
else:

    #quant. de digitos
    num_str = str(num)
    dgts = 0
    for i in num_str:
        dgts += 1
    
    #calculando potencia
    soma = 0
    for i in num_str:
        dgt_int = int(i)
        pot = 1
        
        #digito int^pot
        for _ in range(dgts):
            pot *= dgt_int
        soma += pot
    
    if soma == num:                                                                             #153
                                                                                                #370
        print(f"- O numero {num} é um número de Armstrong!")                                    #371
    else:
        print(f"- O numero {num} NÂO é um número de Armstrong!")

    