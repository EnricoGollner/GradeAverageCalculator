print('Sistema de cálculo da média de notas lançadas!'
      '\nAo encerrar o progrma, será apresentada a média geral das notas lançadas.')

# Tamanho do vetor é definido pelo usuário:
t_vetor = int(input('\nDigite aqui quantas notas serão lançadas para cada aluno: '))
s_geral = 0  # Somará todas as notas lançadas até o encerramento do sistema
i_geral = 0  # Contará quantas notas foram lançadas até o encerramento
opcao = 1
while opcao == 1:
    nome_aluno = input('\nDigite o nome do aluno: ')
    notas = []  # Vetor que armazena as notas
    soma_i = 0  # Soma das notas índividuais
    for i in range(t_vetor):
        n = float(input(f'Digite a {i + 1}° nota do aluno: '))
        if n == 401:
            break  # quebra e não conta a entrada do código e vai para os cálculos e teste
        soma_i += n
        notas.append(n)
    media = soma_i / t_vetor
    s_geral += soma_i
    i_geral += t_vetor
    print('A média correspondente às notas de {} é: {:.1f}'.format(nome_aluno, media))
    # TESTE QUE DIZ SE O ALUNO FOI APROVADO OU NÃO:
    if media < 6:
        print(f'{nome_aluno} está REPROVADO!')
    elif media < 7:
        print(f'{nome_aluno} tem direito de realizar uma prova de recuperação')
    else:
        print(f'{nome_aluno} foi APROVADO!')
    opcao = int(input('\n1-Caso deseje tirar a média das notas de outro aluno'
                      '\n2-Caso deseje encerrar o programa'
                      '\nDigite a opção que deseja: '))
    while (opcao != 1) and (opcao != 2):
        print('\n[!ERRO!] Opção inválida!')
        opcao = int(input('1-Caso deseje tirar a média das notas de outro aluno'
                          '\n2-Caso deseje encerrar o programa'
                          '\nDigite uma opção válida: '))
    if opcao == 2:
        print('\n[Programa finalizado]')
        media_geral = s_geral / i_geral
        print('')
        print('='*65)
        print('A média geral das notas lançadas é:'.center(65))
        print(f'|{media_geral}|'.center(65))
        print('='*65)
        break
