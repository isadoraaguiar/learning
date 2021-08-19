notaA = float(input(''))
notaB = float(input(''))
pesoA = 3.5
pesoB =  7.5

media = ((notaA*pesoA)+(notaB*pesoB))/11

media_round = round(media, 5)

print(f'MEDIA = {media_round:.5f}')

#round arrendoa a média em 5 casas decimais.
# :.5f : obrigada o print a representar 5(ou número dado) de casas decimais. 