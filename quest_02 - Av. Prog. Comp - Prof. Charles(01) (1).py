import sys
nums = input('Insira dois valores para determinar o MDC deles: ')
nums = nums.split(',') 

#verificando quant. de valores.
if len(nums) == 2:
    if nums[0].isdigit() and nums[1].isdigit():

        #convertendo em inteiro.
        if int(nums[0]) > int(nums[1]):
            numerador = int(nums[0])
            denominador = int(nums[1])
        else:
            numerador = int(nums[1])
            denominador = int(nums[0])
        
        print(f'numerador = {numerador} e denominador = {denominador}')
        
        #verificando se x e y negativo ou 0.
        if 0 < denominador or 0 < numerador:

            #calculo
            while denominador != 0:
                resto = numerador % denominador
                numerador = denominador
                denominador = resto
                
        else: 
            sys.exit('valor errado!')
            
            
    else: 
        sys.exit('erro! náo é dígito!')

else: 
    sys.exit('nao tem dois valores!')
print(f'o mdc: {numerador}')