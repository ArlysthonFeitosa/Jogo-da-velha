tabuleiro = [['_','_','_'],['_','_','_'],['_','_','_']]
historicoTab = []
ganhadores = []
ganhar = False
jogador1 = "X"
jogador2 = "O"



'''Funções'''
def escolherOpcaoEOrientar():
    print()
    print('PARA JOGAR DIGITE 1 ')
    print()
    print('PARA VER O HISTÓRICO DIGITE 2')
    print()
    print("PARA ENCERRAR DIGITE 3")
    print()
    opcao = int(input("Digite sua opção: "))

    while opcao != 3:
        if opcao == 1:
            limparTabuleiro()
            jogar()
            
        
        if opcao == 2:
            mostrarHistorico()


        if opcao ==  3:
          print("Fim do jogo!")


        print()
        print('PARA JOGAR DIGITE 1 ')
        print()
        print('PARA VER O HISTÓRICO DIGITE 2')
        print()
        print("PARA ENCERRAR DIGITE 3")
        print()
        opcao = int(input("Digite sua opção: "))



def jogar():
    
    while(True):
        mostrarTabuleiro()
        inserirLinhaColuna(jogador1)

        if(checarSeGanhou(jogador1) == True):
            break
            
        mostrarTabuleiro()
        inserirLinhaColuna(jogador2)

        if(checarSeGanhou(jogador2) == True):
            break



def mostrarTabuleiro():
    print('-------------------------JOGO DA VELHA-------------------------')
    for i in range(0,3):
        print()
        print('                         ',
              tabuleiro[i][0],'|', tabuleiro[i][1],'|', tabuleiro[i][2])
    print()



def inserirLinhaColuna(jogador):
    linha1 = int(input('JOGADOR '+ jogador+' | DIGITE A LINHA: '))
    coluna1 = int (input('JOGADOR '+ jogador+' | DIGITE A COLUNA: '))
    print()

    tabuleiro[linha1 - 1][coluna1 - 1] = jogador



def limparTabuleiro():
    for i in range(0,3):
        for j in range(0,3):
            tabuleiro[i][j] = '_'



def mostrarHistorico():
    numeroDePartidas = len(historicoTab)
    for a in range(0,numeroDePartidas):
        print('-------------------------PARTIDA----------------------------------'.format(a+1))
        print(ganhadores[a])
        for l in range(0,3):
            print('')
            print ('                         ',
                     historicoTab[a][l][0],'|', historicoTab[a][l][1],'|', historicoTab[a][l][2])
            print()



def checarSeGanhou(jogador):
    velha = darVelha()
    linha =ganharEmLinha()
    coluna = ganharEmColuna()
    diagonal = ganharEmDiagonal()

    if(velha == True or linha == True or coluna == True or diagonal == True):
        mostrarTabuleiro()
        historicoTab.append(tabuleiro)
        return True

        

def ganharEmLinha():
    for a in range (0,3):
        if tabuleiro[a][0] == 'X' and tabuleiro[a][1] == 'X' and tabuleiro[a][2] == 'X':
            print('Jogador 1 Ganhou!')
            ganhadores.append("jogador 1 ganhou!")
            return True
            
        if tabuleiro[a][0] == 'O' and tabuleiro[a][1] == 'O' and tabuleiro[a][2]== 'O':
            print('Jogador 2 Ganhou!')
            ganhadores.append("jogador 2 ganhou!")
            return True
        
    return False



def ganharEmColuna():
    for k in range (0,3):
        if tabuleiro[0][k] == 'X' and tabuleiro[1][k] == 'X' and tabuleiro[2][k] == 'X' :
            print('Jogador 1 Ganhou!')
            ganhadores.append("jogador 1 ganhou!")
            return True
                  
        if tabuleiro[0][k] == 'O' and tabuleiro[1][k] == 'O' and tabuleiro[2][k] == 'O' :
            print('Jogador 2 Ganhou!')
            ganhadores.append("jogador 2 ganhou!")            
            return True
    return False



def ganharEmDiagonal():
    if tabuleiro[0][0]== 'X' and tabuleiro[1][1]== 'X' and tabuleiro[2][2] == 'X':
        print ('Jogador 1 Ganhou!')
        ganhadores.append("jogador 1 ganhou!")
        return True
          
    if tabuleiro[0][2]== 'X' and tabuleiro[1][1]== 'X' and tabuleiro[2][0] == 'X':
        print ('Jogador 1 Ganhou!')
        ganhadores.append("jogador 1 ganhou!")
        return True
                  
    if tabuleiro[0][0]== 'O' and tabuleiro[1][1]== 'O' and tabuleiro[2][2] == "O":
        print ('Jogador 2 Ganhou!')
        ganhadores.append("jogador 2 ganhou!")
        return True
          
    if tabuleiro[0][2] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][0] == 'O':
        print('Jogador 2 Ganhou!')
        ganhadores.append("jogador 2 ganhou!")
        return True

    return False



def darVelha():
    if (tabuleiro[0][0] != '_' and tabuleiro[0][1] != '_'and tabuleiro[0][2] != '_'):
        if(tabuleiro[1][0] != '_' and tabuleiro[1][1] != '_' and tabuleiro[1][2] != '_'):
            if (tabuleiro[2][0] != '_' and tabuleiro[2][1] != '_' and tabuleiro[2][2] != '_'):
                if (ganharEmLinha() == False and ganharEmColuna() == False and ganharEmDiagonal() == False):
                    print ("# Deu velha #")
                    ganhadores.append("Velha")
                    return True
    return False



escolherOpcaoEOrientar()

        







    
