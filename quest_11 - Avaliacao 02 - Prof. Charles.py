import sys

# Solicitar a posição inicial de X e Y
x_i = int(input('Insira o valor inicial de X: '))
y_i = int(input('Insira o valor inicial de Y: '))
x = x_i
y = y_i

# Lista de movimentos validos
lst_mov = ['U', 'D', 'R', 'L', 'O', 'N', 'E', 'W']

# Lista para armazenar os movimentopos válidos realizados
lst_movs = []
mov_val = 0

# Solicitar os movimentos a serem realizados
print(' - U (cima) - D (baixo) - R (direita) \n - L (esquerda) - O (noroeste) - N (nordeste) \n - E (sudeste) - W (sudoeste).')

while True:
    mov_ = input("Insira entre (U, D, R, L, O, N, E, W) para movimentar o robô, ou digite 'fim' para parar: ").upper()
    
    if mov_ == 'FIM':
        break
    
    if mov_ in lst_mov:
        if mov_ == 'U':
            y += 1
        elif mov_ == 'D':
            y -= 1
        elif mov_ == 'R':
            x += 1
        elif mov_ == 'L':
            x -= 1
        elif mov_ == 'O':
            x -= 1
            y += 1
        elif mov_ == 'N':
            x += 1
            y += 1
        elif mov_ == 'E':
            x += 1
            y -= 1
        elif mov_ == 'W':
            x -= 1
            y -= 1
        
        mov_val += 1
        lst_movs.append(mov_)
    else:
        print("Erro! Insira um movimento válido!!")

print(f'- Quantidade de movimentos válidos: {mov_val}')
print(f'- X inicial: {x_i} - X final: {x}')
print(f'- Y inicial: {y_i} - Y final: {y}')
print(f'- Movimentos válidos: {lst_movs}')

#verificando quadrante inicial
if x_i > 0 and y_i > 0:
    print('Quadrante inicial: Primeiro quadrante')
elif x_i < 0 and y_i > 0:
    print('Quadrante inicial: Segundo quadrante')
elif x_i < 0 and y_i < 0:
    print('Quadrante inicial: Terceiro quadrante')
elif x_i > 0 and y_i < 0:
    print('Quadrante inicial: Quarto quadrante')
else:
    print('Quadrante inicial: No centro do eixo X ou Y')

#verificando quadrante final
if x > 0 and y > 0:
    print('Quadrante final: Primeiro quadrante')
elif x < 0 and y > 0:
    print('Quadrante final: Segundo quadrante')
elif x < 0 and y < 0:
    print('Quadrante final: Terceiro quadrante')
elif x > 0 and y < 0:
    print('Quadrante final: Quarto quadrante')
else:
    print('Quadrante final: No centro do eixo X ou Y')