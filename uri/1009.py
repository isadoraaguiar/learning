nv = input('')
sf = float(input(''))
tv = float(input(''))

comissao = (tv*0.15)
salario = round(comissao+sf, 2)

print(f'TOTAL = R$ {salario:.2f}')


