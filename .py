#questao 1


#questao 2
taxa = 0
valor = float(input('Digite O Valor da Compra: '))
parcelas = int(input('Digite A Quantidade De Parcelas: '))
if valor > 500:
    taxa = -(0.1)
elif parcelas > 5:
    taxa = 0.08
valor_final = valor + (valor * taxa)
valor_parcela = valor_final // parcelas
print(f'> O Valor Original é: {valor}')
print(f'> O Valor Final é: {valor_final}')
print(f'> O Valor Das Parcelas São Aproximadamente: {valor_parcela}')