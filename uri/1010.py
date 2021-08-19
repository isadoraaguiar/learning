peca1_c, peca1_n, peca1_v = input('').split(' ')
peca2_c, peca2_n, peca2_v = input('').split(' ')

total = (float(peca1_v) * int(peca1_n)) + (float(peca2_v) * int(peca2_n))

print(f'VALOR A PAGAR: R$ {round(total, 2):.2f}')