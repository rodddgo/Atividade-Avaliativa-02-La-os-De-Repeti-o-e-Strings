import sys
m_inicial = int(input('- Insira o valor da massa inicial (em gramas) do produto: '))

#verificando se num é maior ou igual a zero.
if m_inicial <= 0:
    sys.exit('Erro! Insira um valor Válido')
else:
    #contabilizando tempo.
    seg = 0 
    m_final = m_inicial
    while 0.5 < m_final > 0:
        m_final *= 0.5
        seg += 50
    hr = seg // 3600
    min = (seg % 3600) // 60
    seg = seg % 60
    print(f'- Tempo de decaimento: {hr}:{min}:{seg} ')

        
        