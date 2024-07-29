def inicio():
    print('\nOs alunos estão em fila')
    print('\nO primeiro da fila é atendido')
    conferir_carteirinha()

def conferir_carteirinha():
    carteirinha=input('\nO aluno possui carteirinha?\nDigite "Sim" ou "Não"\nR:').strip().capitalize()
    if carteirinha=='Sim':
        primeira_ves()
    elif carteirinha == 'Nao' or carteirinha=='Não':
        print('\nPROVIDENCIE A CARTEIRINHA E VOLTE PARA A FILA.')
        inicio()
    else:
        print('OPÇÃO INVÁLIDA.')
        conferir_carteirinha()

def primeira_ves():
    primeira=input('\nÉ a primeira ves que este aluno está comendo?\nDigite "Sim" ou "Não"\nR:').strip().capitalize()
    if primeira=='Sim':
        tem_lanche()
    elif primeira == 'Não' or primeira == 'Nao':   
        pegou_lanche()
    else:
        print('OPÇÃO INVÁLIDA.')
        primeira_ves()

def pegou_lanche():
    nao_lanche=input('\nHá alguém na fila que ainda não pegou lanche?\nDigite "Sim" ou "Não"\nR:').strip().capitalize()
    if nao_lanche=='Sim':
        print('\nAguarde todos comerem.')
        print('\nvolte para a fila.')
        inicio()
    elif nao_lanche == 'Não' or nao_lanche == 'Nao':
        tem_lanche()
    else:
        print('OPÇÃO INVÁLIDA.')
        pegou_lanche()

def tem_lanche():
    lanche=input('\nAinda tem lanche?\nDigite "Sim" ou "Não"\nR:').strip().capitalize()
    if lanche=='Sim':
        é_recreio()
    elif lanche == 'Não' or lanche == 'Nao':
        terminar()
    else:
        print('OPÇÃO INVÁLIDA.')
        tem_lanche()

def é_recreio():
    recreio=input('\nAinda é recreio?\nDigite "Sim" ou "Não"\nR:').strip().capitalize()
    if recreio=='Sim':
        print('\n1-Faça a leitura da carteirinha.\n2-Devolva a carteirinha\n3-Libere para pegar o lanche\n4-O aluno come o lanche')
        deseja_repetir()
    elif recreio == 'Não' or recreio == 'Nao':
        print('Vá para a aula.')
    else:
        print('OPÇÃO INVÁLIDA.')
        é_recreio()

def deseja_repetir():
    repetir=input('\ndeseja repetir?\nDigite "Sim" ou "Não"\nR:').strip().capitalize()
    if repetir=='Sim':
        print('\nVolte para a fila.\n')
        inicio()
    elif repetir == 'Não' or repetir == 'Nao':
        terminar()
    else:
        print('OPÇÃO INVÁLIDA.')
        deseja_repetir()

def terminar():
    print('\nAguarde o término do recreio\nVá para a sala')
    
inicio()