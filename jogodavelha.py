import random  # Importa o módulo random para gerar jogadas aleatórias para a IA

# Função para exibir o tabuleiro do jogo da velha
def exibir_tabuleiro(tabuleiro):
    
    # Exibe o tabuleiro do jogo em formato visual para o jogador.
    # O tabuleiro é uma lista de listas contendo os símbolos "X", "O" ou " " (espaços vazios).
    
    for linha in tabuleiro:
        # Junta os elementos da linha com "|" entre eles e exibe
        print("|".join(linha))
        # Exibe uma linha de separação entre as linhas do tabuleiro
        print("-" * 5)

# Função para verificar se houve vitória
def verificar_vitoria(tabuleiro, jogador):
    
    # No caso verifica se o jogador (X ou O) venceu o jogo.
    # Um jogador vence quando 3 dos seus símbolos estão em linha, coluna ou diagonal.
    # Irá retorna True se vencer, senão retorna False.
    
    # Verificar se o jogador venceu em alguma linha
    for linha in tabuleiro:
        if linha.count(jogador) == 3:  # Se todos os elementos da linha forem do jogador
            return True

    # Verificar se o jogador venceu em alguma coluna
    for col in range(3):  # Verifica as 3 colunas
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] == jogador:
            return True

    # Verificar se o jogador venceu nas diagonais
    # Diagonal principal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    # Diagonal secundária
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    # Se nenhuma condição de vitória for atendida, retorna False
    return False

# Função para verificar se houve empate
def verificar_empate(tabuleiro):
    
    #Verifica se o jogo terminou em empate.
    # Um empate ocorre quando todos os espaços do tabuleiro estão preenchidos sem que haja um vencedor.
    # Retorna True se o jogo empatar, caso contrário, retorna False.
    
    for linha in tabuleiro:
        if " " in linha:  # Se ainda houver espaços vazios no tabuleiro, não há empate
            return False
    return True  # Se todas as posições estiverem preenchidas, o jogo empata

# Função para a jogada da IA
def jogada_ia(tabuleiro):
    
    # Define a jogada da IA escolhendo uma posição aleatória disponível no tabuleiro.
    # Retorna a linha e a coluna onde a IA jogará.
    
    # Lista de jogadas possíveis: todas as posições que ainda estão vazias (" ")
    jogadas_possiveis = [(i, j) for i in range(3) for j in range(3) if tabuleiro[i][j] == " "]
    # Escolhe aleatoriamente uma das posições vazias
    return random.choice(jogadas_possiveis)

# Função principal que executa o jogo da velha
def jogar():
    
    # Função principal que controla o jogo da velha.
    # Inicializa o tabuleiro, alterna entre o jogador humano (X) e a IA (O), e verifica condições de vitória ou empate.
    # O jogador humano faz a primeira jogada.
    
    # Inicializa o tabuleiro com 3x3 posições vazias
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    # Definir símbolos para o jogador humano e a IA
    jogador_humano = "X"  # O jogador humano sempre joga com "X"
    jogador_ia = "O"      # A IA joga com "O"
    jogo_ativo = True     # Controle do loop principal do jogo, continua enquanto for True

    # Loop principal do jogo, alternando jogadas até o jogo terminar
    while jogo_ativo:
        # Exibir o tabuleiro atual para o jogador humano
        exibir_tabuleiro(tabuleiro)
        print("Sua vez, jogador X.")

        # Receber entrada do jogador humano para linha e coluna
        linha = int(input("Escolha a linha (0, 1, 2): "))
        coluna = int(input("Escolha a coluna (0, 1, 2): "))

        # Verifica se a posição escolhida está vazia
        if tabuleiro[linha][coluna] == " ":
            # Se estiver vazia, o jogador humano faz sua jogada
            tabuleiro[linha][coluna] = jogador_humano
        else:
            # Se a posição estiver ocupada, o jogador precisa escolher novamente
            print("Essa posição já está ocupada! Tente novamente.")
            continue  # Volta para a escolha da jogada do jogador

        # Verificar se o jogador humano venceu após a jogada
        if verificar_vitoria(tabuleiro, jogador_humano):
            exibir_tabuleiro(tabuleiro)
            print("Parabéns! Você venceu!")
            jogo_ativo = False  # Termina o jogo se houver vitória
            break

        # Verificar se houve empate após a jogada do jogador humano
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            jogo_ativo = False  # Termina o jogo se houver empate
            break

        # Jogada da IA (após a jogada do jogador humano)
        print("Turno da IA (O)...")
        # A IA escolhe uma jogada aleatória
        linha_ia, coluna_ia = jogada_ia(tabuleiro)
        # A IA marca sua jogada no tabuleiro
        tabuleiro[linha_ia][coluna_ia] = jogador_ia

        # Verificar se a IA venceu após sua jogada
        if verificar_vitoria(tabuleiro, jogador_ia):
            exibir_tabuleiro(tabuleiro)
            print("A IA venceu!")
            jogo_ativo = False  # Termina o jogo se a IA vencer
            break

        # Verificar se houve empate após a jogada da IA
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            jogo_ativo = False  # Termina o jogo se houver empate
            break

# Agora chamar a função principal
jogar()