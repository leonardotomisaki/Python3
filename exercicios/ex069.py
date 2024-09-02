idade = homens = mulheres = dezoito = 0
sexo = continuar = ''
print('-=' * 10)
print('CADASTRO')
print('-=' * 10)
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()
        print("-=" * 10)
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if idade > 18:
        dezoito = dezoito + 1
    if idade < 20 and sexo == 'F':
        mulheres = mulheres + 1
    if sexo == 'M':
        homens = homens + 1
    if continuar == 'N':
        break
print('========== FIM DO PROGRAMA ==========')
print(f'Ao todo foram cadastrados {dezoito} pessoas com mais de 18 anos;')
print(f'Foram cadastrados {homens} homens;')
print(f'E foram cadastrados {mulheres} mulheres com menos de 18 anos.')
