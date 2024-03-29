import random
import filmeInfos
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_hangman(chances):
    stages = [  # estágio 6 (final)
                """
                ==============================
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                ==============================
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                ==============================
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                ==============================
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                ==============================
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                ==============================
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0 (inicial)
                """
                ==============================
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

def display_menu():
    print('''
    Bem-vindo(a) ao jogo da forca!
    Adivinhe o nome do filme!
    1 - jogar
    2 - adicionar filme
    3 - ver filmes
    4 - remover filme
    5 - sair do jogo
    ''')
    
def jogar(palavra, palavra_escondida, chances, letras_erradas, dicas, vez):
    print('Vamos começar!')
    while chances > 0:
        # print

        print(display_hangman(chances))

        print(''.join(palavra_escondida))
        print(f'\nChances restantes: {chances}')
        print('Letras erradas', " ".join(letras_erradas))
        if vez != 0:
            print(f'Dicas: {dicas[:vez]}') if vez < 3 else print(f'Você usou todas as dicas!\n Dicas:{dicas}')

        # input
        tentativa = input('Digite uma letra: ').lower()

        # condicional teste letras
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    palavra_escondida[index] = letra
                index += 1
            if ''.join(palavra_escondida) == palavra:
                print(''.join(palavra_escondida))
                print('Parabéns! Você ganhou!')
                break
        elif tentativa == 'dica':
                # print(dicas[:vez+1]) if vez < 3 else print(f'Você usou todas as dicas!\n{dicas}')
                vez += 1
        else:
            if tentativa in letras_erradas:
                print('Você já tentou essa letra!')
            else:
                letras_erradas.append(tentativa)
                chances -= 1
                  
    if chances == 0:
        print('\nVocê perdeu!')
        print(f'A filme era: {palavra}')

def jogo():
    limpa_tela()
    display_menu()
    
    # dicas dos filmes
    infos = {'La la land': ['Ano: 2016','Direcao: Damien Chazelle','Cast: emma stone, ryan gosling'], 'The handmaiden': ['Ano: 2016', 'Direcao: Park Chan-wook', 'Cast: Kim Min-hee, Ha Jung-woo, Cho Jin-woong'], 'Scream': ['Ano: 1996', 'Direcao: Wes Craven', 'Cast: Neve Campbell, Courteney Cox, David Arquette'], 'Poor things': ['Ano: 2023', 'Direcao: Yorgos Lanthimos', 'Cast: Emma Stone, Mark Ruffalo, Willem Dafoe']}
    
    while True:  

        palavra = random.choice(list(infos.keys()))
        dicas = infos[palavra]
        vez = 0
        palavra_escondida = ['_' if letra != ' ' else ' ' for letra in palavra ] # operador ternario e comprehension list
        chances =  6
        letras_erradas = []
        palavra = palavra.lower()

        opcao = input('Digite uma opção: \n')
        if opcao == '1':
            print('jogar\n')
            jogar(palavra, palavra_escondida, chances, letras_erradas, dicas, vez)
        elif opcao == '2':
            print('adicione um filme\n')
            filmeInfos.addFilme(infos)
        elif opcao == '3':
            print('lista de filmes\n')
            for filme in infos.keys():
                print(filme)
        elif opcao == '4':
            remover = input('digite o filme a ser removido: ')
            if remover in infos:
                infos.pop(remover)
                print('filme removido com sucesso!')
            else:
                print('filme nao encontrado!')
        elif opcao == '5':
            print('saindo do jogo...')
            exit()

        
  

jogo()
    
