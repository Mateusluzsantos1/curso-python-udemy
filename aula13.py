nome = 'Mateus Luz'
altura  = 1.70
peso  = 58.5
imc = peso / altura ** 2


linha_1 = f'{nome}  tem  {altura: .2f} de altura'

linha_2 = f'pesa  {peso}  kg e seu IMC é'

linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2 )
print(linha_3)