nome = input('Qual é o seu nome?')
idade = input('Qual a sua idade?')
altura = input('Qual a sua aultura?')
sobrenome = input('Qual a seu sobrenome?') 
# print(nome, idade, altura, sobrenome)


salvar_no_banco({
    'nome': nome,
    'idade': idade,
    'altura': altura,
    'sobrenome': sobrenome
})

