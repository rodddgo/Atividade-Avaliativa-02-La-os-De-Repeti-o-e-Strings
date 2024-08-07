import sys

v_int = input('- Insira um valor inteiro positivo: ')

#verificar se é digito.
if v_int.isdigit() and int(v_int) > 0:

    #contar quantidade de dígitos.
    quant_num = 0 
    for element in v_int: 
        quant_num += 1 
else:
    sys.exit('Erro! Insira um valor INTEIRO POSITIVO')

print(f'O valor informado possui {quant_num} dígitos.')