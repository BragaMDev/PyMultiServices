print('===== Questão 1 =====')
nome = input('Digite Seu Nome: ')
idade = int(input('Digite Sua Idade: '))
salario = float(input('Digite Seu Salário: '))
nome.lower()
print(f'> Seu Nome é: {nome.title()}')
print(f'> Sua Idade é: {idade}')
print(f'> Seu Salário é: {salario}')
if idade >= 18:
    print('> Maior De Idade')
else:
    print('> Menor De Idade')
if salario >= 3000:
    print(f'> Seu Salário é: {salario:.2f} e é Maior ou Igual que R$3000.00')
else:
    print(f'> Seu Salário de {salario} é Menor que R$3000.00')

print('===== Questão 2 =====')
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
print('===== Questão 3 =====')
numeros = []
soma = 0
soma_pares = 0
soma_impar = 0
for i in range(10):
    numero = int(input('Digite Um Numero Inteiro: '))
    numeros.append(numero)
for numero in numeros:
    if numero % 2 == 0:
            soma_pares += 1
    elif numero % 2 != 0:
            soma_impar += 1
for numero in numeros:
      soma += numero
print(f'> A Quantidade De Números Pares É: {soma_pares}')   
print(f'> A Quantidade De Números Ímpares É: {soma_impar}')
print(f'> O Maior Número Digitado É: {max(numeros)}')
print(f'> O Menor Número Digitado É: {min(numeros)}')
media = soma / len(numeros)
print(f'> A Média Aproximadamente É: {media}')

print('===== Questão 4 =====')
for i in range(3):
            usuario = input('Digite seu Nome de Usuário: ')
            senha = input('Digite Sua Senha: ')

            if usuario == 'admin' and senha == '1234':
                print('> Acesso Permitido')
                break
            else:
                print('> Acesso Negado')
                if i == 2:
                    print('> Conta Bloqueada')
print('===== Questão 5 =====')
alunos = []
for i in range(5):
        aluno = input('Digite o Nome Do Aluno: ')
        nota1 = int(input('Digite a Primeira Nota: '))
        nota2 = int(input('Digite a Segunda Nota: '))
        nota3 = int(input('Digite a Terceira Nota: '))

        def calcular_media():
            soma = (nota1 + nota2 + nota3) / 3
            return soma
        
        resultado = calcular_media()
        if calcular_media() >= 7:
            situacao = 'Aprovado'
        elif calcular_media() >= 5 and calcular_media() < 7:
            situacao = 'Recuperação'
        elif calcular_media() < 5:
            situacao = 'Reprovado'
        else:
            print('> Digite as Notas Novamente')

        alunos.append((aluno,situacao,resultado))
aluno.lower()
print('===== Sistema De Alunos =====')
for aluno,situacao,resultado in alunos:
    print(f'> Aluno: {aluno.title()}')
    print(f'> Sua Média É: {resultado}')
    print(F'> Situação Acadêmica: {situacao}')

print('===== Questão 6 =====')
numeros = []
soma = 0
soma_pares = 0
soma_impar = 0
for i in range(10):
    numero = int(input('Digite Um Numero Inteiro: '))
    numeros.append(numero)
for numero in numeros:
    if numero % 2 == 0:
            soma_pares += 1
    elif numero % 2 != 0:
            soma_impar += 1
for numero in numeros:
      soma += numero
      print(f'> Número: {numero}')
print(f'> A Quantidade De Números Pares É: {soma_pares}')   
print(f'> A Quantidade De Números Ímpares É: {soma_impar}')
print(f'> O Maior Número Digitado É: {max(numeros)}')
print(f'> O Menor Número Digitado É: {min(numeros)}')
media = soma / len(numeros)
print(f'> A Média Aproximadamente É: {media}')
numeros.sort()
print(f'> Ordem: {numeros}')

print('===== Questão 7 =====')
alunos = []
cont_aprov = 0
cont_rec = 0
cont_reprovados = 0
for i in range(5):
        aluno = input('Digite o Nome Do Aluno: ')
        nota1 = int(input('Digite a Primeira Nota: '))
        nota2 = int(input('Digite a Segunda Nota: '))
        nota3 = int(input('Digite a Terceira Nota: '))

        def calcular_media():
            soma = (nota1 + nota2 + nota3) / 3
            return soma
        
        resultado = calcular_media()
        if calcular_media() >= 7:
            situacao = 'Aprovado'
            cont_aprov += 1
        elif calcular_media() >= 5 and calcular_media() < 7:
            situacao = 'Recuperação'
            cont_rec += 1
        elif calcular_media() < 5:
            situacao = 'Reprovado'
            cont_reprovados += 1
        else:
            print('> Digite as Notas Novamente')

        alunos.append((aluno,situacao,resultado))
aluno.lower()
print('===== Sistema De Alunos =====')
for aluno,situacao,resultado in alunos:
    print(f'> Aluno: {aluno.title()}')
    print(f'> Sua Média É: {resultado}')
    print(F'> Situação Acadêmica: {situacao}')
print(f'> Quantidade De Reprovados: {cont_reprovados}')
print(f'> Quantidade De Aprovados: {cont_aprov}')
print(f'> Quantidade De Recuperação: {cont_rec}')
alunos.sort(reverse=True)
aluno.lower()
print(f'> Aluno Com Melhor Média: {alunos[0][0].title()} Melhor Média: {alunos[0][2]}')

print('===== Questão 8 =====')
while True:
    print('===== Calculadora =====')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')
    ope = int(input('Digite A Operação: '))
    def calcular_soma():
        print('===== Soma =====')
        num1 = float(input('Digite O Primeiro Número: '))
        num2 = float(input('Digite O Segundo Número: '))
        soma = num1 + num2
        return soma
    def calcular_sub():
        print('===== Subtração =====')
        num1 = float(input('Digite O Primeiro Número: '))
        num2 = float(input('Digite O Segundo Número: '))
        menos = num1 - num2
        return menos
    def calcular_multi():
        print('===== Multiplicação =====')
        num1 = float(input('Digite O Primeiro Número: '))
        num2 = float(input('Digite O Segundo Número: '))
        vezes = num1 * num2
        return vezes
    def calcular_div():
        print('===== Divisão =====')
        num1 = float(input('Digite O Primeiro Número: '))
        num2 = float(input('Digite O Segundo Número: '))
        if num2 == 0:
            print('> Erro: Divisão por 0')
            return None
        divisao = num1 / num2
        return divisao
    if ope == 1:
         resultado = calcular_soma()
         print(f'> Resultado Da Soma: {resultado}')
    elif ope == 2:
         resultado = calcular_sub()
         print(f'> Resultado Da Subtração: {resultado}')
    elif ope == 3:
         resultado = calcular_multi()
         print(f'> Resultado Da Multiplicação: {resultado}')
    elif ope == 4:
         resultado = calcular_div()
         print(f'> Resultado Da Divisão: {resultado}')
    elif ope == 5:
         print(f'> Saiu')
         break
    else:
        print('> Digite Novamente')

print('===== Questão 9 =====')
frase = input('Digite Uma Frase: ')
contagem_a = frase.count('a')
contagem_e = frase.count('e')
contagem_i = frase.count('i')
contagem_o = frase.count('o')
contagem_u = frase.count('u')
total = contagem_a + contagem_e + contagem_i + contagem_o + contagem_u
contagem_espaço = frase.count(' ')
palavras = frase.split()  
qtd_palavras = len(palavras)
palavras.reverse()   
print(f'> Quantidade total de caracteres: {len(frase)}')
print(f'> Quantidade de vogais A: {contagem_a}')
print(f'> Quantidade de vogais E: {contagem_e}')
print(f'> Quantidade de vogais I: {contagem_i}')
print(f'> Quantidade de vogais O: {contagem_o}')
print(f'> Quantidade de vogais U: {contagem_u}')
print(f'> Quantidade de vogais totais: {total}')
print(f'> Quantidade de espaços: {contagem_espaço}')
print(f'> Quantidade de Palavras: {qtd_palavras}')
frase = frase.upper()
print(f'> Frase em Maiúscula: {frase}')
print(f'> Frase invertida: {" ".join(palavras)}')


print('===== Questão 10 =====')
sistema = []
while True:
    print('===== Menu =====')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Buscar produto')
    print('4 - Remover produto')
    print('5 - Encerrar sistema')
    servico = int(input('Selecione O Serviço Desejado: '))
    if servico == 1:
        qnt_produtos = int(input('Digite Quantos Produtos Deseja Cadastrar: '))
        for i in range(qnt_produtos):
            produto = input('Digite O Nome Do Produto: ')
            qntd = int(input('Digite A Quantidade Do Produto: '))
            preco = float(input('Digite O Preço Do Produto: '))
            sistema.append((produto, qntd, preco))
        print('> Produto(s) Cadastrado(s)')
    elif servico == 2:
        for produto, qntd, preco in sistema:
            print(f'> Produto: {produto}')
            print(f'> Quantidade: {qntd}')
            print(f'> Preço: {preco}')
    elif servico == 3:
        busca = input('Digite o Nome Do Produto: ')
        busca = busca.lower().strip()
        for produto, qntd, preco in sistema:
            if produto == busca:
                print('> Produto encontrado.')
                print(f'> Produto: {produto}')
                print(f'> Quantidade: {qntd}')
                print(f'> Preço: {preco}')
                break
        else:
            print('> Produto não cadastrado.')
    elif servico == 4:
        remover = input('Digite o nome do produto para remover: ').lower().strip()
        for p in sistema:
            if p[0].lower().strip() == remover:
                sistema.remove(p)
                print('> Produto removido!')
                break

    elif servico == 5:
        print('> Encerrado')
        break