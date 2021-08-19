nota_a = float(input(''))
nota_b = float(input(''))
nota_c= float(input(''))
peso_a= 2.0
peso_b= 3.0
peso_c= 5.0

media = ((nota_a*peso_a)+(nota_b*peso_b)+(nota_c*peso_c))/10.0
media_round = round(media, 1)

print(f'MEDIA = {media_round:.1f}')

